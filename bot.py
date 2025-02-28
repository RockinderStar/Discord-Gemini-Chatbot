import os
import discord
from discord.ext import commands
import google.genai as genai
from dotenv import load_dotenv

# Load environment variables from .env file, you will have to get your own API keys :D
load_dotenv()

# Configuring Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialise Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = 'gemini-2.0-flash-001'

# Store conversation history per channel
conversation_history = {}
MAX_HISTORY_LENGTH = 10


async def generate_response(prompt, channel_id):
    """Generate a response using the Gemini API"""
    try:
        if channel_id not in conversation_history:
            conversation_history[channel_id] = []

        chat = client.models.generate_content(
            model=MODEL_NAME,
            contents=[*conversation_history[channel_id], prompt],
        )

        response_text = chat.text

        conversation_history[channel_id].append(prompt)
        conversation_history[channel_id].append(response_text)

        if len(conversation_history[channel_id]) > MAX_HISTORY_LENGTH * 2:
            conversation_history[channel_id] = conversation_history[channel_id][-MAX_HISTORY_LENGTH * 2:]

        return response_text
    except Exception as e:
        return f"Error generating response: {str(e)}"


@bot.event
async def on_ready():
    """Event fired when the bot is ready"""
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')


@bot.event
async def on_message(message):
    """Event fired when a message is sent in a channel the bot can see"""
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    # Respond to mentions (only if it's NOT a command)
    if bot.user in message.mentions and not message.content.startswith("!"): # only run if it is a mention and not a command.

        content = message.content.replace(f'<@{bot.user.id}>', '').strip()

        if not content:
            await message.channel.send("How can I help you today?")
            return

        async with message.channel.typing():
            response = await generate_response(content, str(message.channel.id))
            # Discord has a message character limit of 2000 characters. This if statement checks if the response is within that limit
            if len(response) <= 2000:
                await message.channel.send(response)
            else:
                chunks = [response[i:i + 2000] for i in range(0, len(response), 2000)]
                for chunk in chunks:
                    await message.channel.send(chunk)

# Run the bot
if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
