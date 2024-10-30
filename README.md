Achievement Tracker Telegram Bot
A Telegram bot that helps users track their educational achievements, courses, and certifications. The bot collects information about achievements including title, description, duration, provider, course details, project information, and certificate image names.
Features

Record educational achievements
Store achievement details including:

`Achievement title`
`Description`
`Duration`
`Provider (e.g., Coursera, Udemy)`
`Course name`
`Project details`
`Certificate image name`


MongoDB integration for data persistence
Conversation-based user interface
Easy to deploy on Railway

Prerequisites:

Python 3.7+
Telegram Bot Token (from @BotFather)
MongoDB URI (from MongoDB Atlas)
GitHub account
Railway account

Environment Variables
Create a .env file in your project root with the following variables:
`TELEGRAM_BOT_TOKEN = your_bot_token_here`
`MONGO_URI= your_mongodb_uri_here`
Local Development

Clone the repository:

bash: `git clone https://github.com/mithun-ctrl/achievement-tracker-bot.git`
cd achievement-tracker-bot

Create and activate a virtual environment:

bash: `python -m venv venv`
source: `venv/bin/activate`  
#On Windows: `venv\Scripts\activate`

Install dependencies:

bash: `pip install -r requirements.txt`

Run the bot:

bash:  `python main.py`
Deployment on Railway

Fork this repository to your GitHub account
Create a Railway account at railway.app
Create a new project in Railway:

Click "New Project"
Select "Deploy from GitHub repo"
Choose your forked repository
Click "Deploy Now"


Add Environment Variables in Railway:

Go to your project's "Variables" tab
Add the following variables:

`TELEGRAM_BOT_TOKEN`
`MONGO_URI`




Railway will automatically deploy your bot when you push changes to your repository

Project Structure:
`achievement-tracker-bot/`
`├── main.py               # Main bot code`
`├── requirements.txt      # Python dependencies`
`├── .env                 # Environment variables (local development)`
`├── .gitignore          # Git ignore file`
`└── README.md           # Project documentation`
Bot Commands

`/start - Start recording a new achievement`
`/cancel - Cancel the current operation`

Contributing

Fork the repository
Create a new branch (git checkout -b feature/improvement)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/improvement)
Create a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.