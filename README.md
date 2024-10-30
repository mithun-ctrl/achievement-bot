# Achievement Tracker Telegram Bot 🎯

A powerful Telegram bot built with Python that helps users track and record their educational achievements, certifications, and courses. The bot stores user achievements in MongoDB and provides a seamless conversation-based interface.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-✓-blue.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-✓-green.svg)

## 📋 Features

- **Comprehensive Achievement Tracking**
  - Achievement title and description
  - Course duration
  - Provider information
  - Course details
  - Project descriptions
  - Certificate image naming

- **User-Friendly Interface**
  - Conversation-based interaction
  - Step-by-step achievement recording
  - Clear instructions and prompts
  - Easy cancellation option

- **Robust Data Management**
  - MongoDB integration
  - Secure data storage
  - Organized data structure
  - Timestamp tracking

- **Error Handling & Logging**
  - Comprehensive error handling
  - Detailed logging system
  - User-friendly error messages
  - Debug information for maintenance

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:
- Python 3.7 or higher installed
- A Telegram account
- A MongoDB database
- Git installed

### Installation Steps

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/achievement-tracker-bot.git
cd achievement-tracker-bot
```

2. **Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**
Create a `.env` file in the root directory:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
MONGO_URI=your_mongodb_uri_here
```

5. **Run the Bot**
```bash
python main.py
```

## 💻 Deployment

### Deploy on Railway

1. **Fork this Repository**
   - Click the Fork button in the top right corner

2. **Set Up Railway**
   - Create an account on [Railway](https://railway.app/)
   - Click "New Project"
   - Select "Deploy from GitHub"
   - Choose your forked repository

3. **Configure Environment Variables**
   - Go to your Railway project
   - Navigate to Variables
   - Add the following:
     - `TELEGRAM_BOT_TOKEN`
     - `MONGO_URI`

4. **Deploy**
   - Railway will automatically deploy your bot
   - Check deployment status in the Deployments tab

## 🛠️ Development Setup

### Getting Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` command
3. Follow the prompts to create your bot
4. Copy the provided token

### Setting Up MongoDB

1. Create a [MongoDB Atlas](https://www.mongodb.com/atlas/database) account
2. Create a new cluster
3. Get your connection string
4. Replace `your_mongodb_uri_here` in `.env`

## 📝 Usage

### Bot Commands

- `/start` - Begin recording a new achievement
- `/cancel` - Cancel the current operation

### Recording an Achievement

1. Start the bot with `/start`
2. Enter achievement title
3. Provide description
4. Specify duration
5. Enter provider name
6. Input course details
7. Describe your project
8. Send certificate image

## 🗂️ Project Structure

```
achievement-tracker-bot/
├── main.py               # Main bot code
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables
├── .gitignore          # Git ignore file
└── README.md           # Documentation
```

## 🔧 Configuration

### Environment Variables

| Variable | Description |
|----------|-------------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token from BotFather |
| `MONGO_URI` | MongoDB connection string |

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/awesome-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add awesome feature'`)
5. Push to the branch (`git push origin feature/awesome-feature`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [pymongo](https://github.com/mongodb/mongo-python-driver)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

## 📫 Contact

If you have any questions or suggestions, feel free to open an issue or contact the maintainers.

## 🔍 Troubleshooting

### Common Issues

1. **Bot Not Responding**
   - Check if your bot token is correct
   - Ensure the bot is running
   - Verify internet connection

2. **MongoDB Connection Issues**
   - Verify MongoDB URI
   - Check IP whitelist in MongoDB Atlas
   - Ensure proper database permissions

3. **Deployment Issues**
   - Verify environment variables in Railway
   - Check deployment logs
   - Ensure all dependencies are listed in requirements.txt
