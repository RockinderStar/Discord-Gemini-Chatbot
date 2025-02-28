# Discord-Gemini-Chatbot
This is a short project trying to integrate the Gemini API into Discord to make a simple chatbot.
The bot is able to maintain conversation history within each Discord Channel, and is also able to handle long AI responses by splitting them into multiple Discord messages.
# Prerequisites
Python 3.9+
Google Gemini API Key
Discord Bot Token

# How to Install
1.  **Clone the repository:**

    ```bash
    git clone [repository URL]
    cd discord-gemini-chatbot
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**

    * **Windows:** `.venv\Scripts\activate`
    * **macOS/Linux:** `source .venv/bin/activate`

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Create a `.env` file in the project directory and add your Discord Bot Token and Google Gemini API Key:**

    ```
    DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
    GEMINI_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY
    ```

    Replace `YOUR_DISCORD_BOT_TOKEN` and `YOUR_GOOGLE_GEMINI_API_KEY` with your actual tokens.

6.  **Run the bot:**

    ```bash
    python bot.py
    ```

    (Replace `bot.py` with the name of your python file)

## Usage

1.  **Invite the bot to your Discord server:**
    * Go to the Discord Developer Portal, select your application, and navigate to the "OAuth2" tab.
    * Select the "bot" scope and "Administrator" Bot Permissions.
    * Copy the generated URL and paste it into your browser.

3.  **Mention the bot:**
    * Type `@BotName [your message]` to have a conversation with the AI.
