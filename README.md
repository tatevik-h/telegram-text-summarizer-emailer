# telegram-text-summarizer-emailer
🤖📲 Telegram bot that summarizes text using OpenAI 🧠✂️ and emails the summary 📧✅

## 🏜️ Features
- Summarize long texts using OpenAI GPT
- Sends summaries directly to your email
- Easy to set up and extend(e.g., LongChain integration)

## 🪂 Quick Start
1. Clone the repo:
   ```
      git clone git@github.com:tatevik-h/telegram-text-summarizer-emailer.git
      cd telegram-text-summarizer-emailer
   ```
2. Install dependencies:
   ```
     pip install -r requirements.txt
   ```
3. Create a ```.env``` file from the example and fill in your secrets:
   ``` .env
     TELEGRAM_TOKEN=your-bot-token
     OPENAI_API_KEY=your-api-key
     EMAIL_ADDRESS=your-email-address
     EMAIL_PASSWORD=your-email-password
   ```
4. Run the bot:
   ```
     python app/bot.py
   ```

## 📚 Tech Stack
- Python3
- OpenAI API
- Telegram Bot API
- SMTP for email
  
