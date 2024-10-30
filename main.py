import os
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
from pymongo import MongoClient
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")

MONGO_URI = os.getenv('MONGO_URI')
if not MONGO_URI:
    raise ValueError("No MONGO_URI found in environment variables")

# MongoDB setup
try:
    client = MongoClient(MONGO_URI)
    # Test the connection
    client.server_info()
    db = client['achievements_db']
    collection = db['achievements']
    logger.info("Successfully connected to MongoDB")
except Exception as e:
    logger.error(f"Error connecting to MongoDB: {str(e)}")
    raise

# Conversation states
ACHIEVEMENT, DESCRIPTION, DURATION, PROVIDER, COURSE, PROJECT, CERTIFICATE = range(7)

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the conversation and ask for achievement."""
    user = update.effective_user
    logger.info(f"User {user.id} started the bot")
    
    await update.message.reply_text(
        f"Hi {user.first_name}! I'll help you record your achievement. "
        "Please enter the achievement title:"
    )
    return ACHIEVEMENT

async def achievement(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store achievement and ask for description."""
    user = update.effective_user
    context.user_data['achievement'] = update.message.text
    logger.info(f"User {user.id} entered achievement: {update.message.text}")
    
    await update.message.reply_text("Great! Now provide a description of your achievement:")
    return DESCRIPTION

async def description(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store description and ask for duration."""
    user = update.effective_user
    context.user_data['description'] = update.message.text
    logger.info(f"User {user.id} entered description")
    
    await update.message.reply_text("How long did it take to complete? (e.g., '3 months', '2 weeks'):")
    return DURATION

async def duration(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store duration and ask for provider."""
    user = update.effective_user
    context.user_data['duration'] = update.message.text
    logger.info(f"User {user.id} entered duration: {update.message.text}")
    
    await update.message.reply_text("Who was the provider? (e.g., 'Coursera', 'Udemy'):")
    return PROVIDER

async def provider(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store provider and ask for course name."""
    user = update.effective_user
    context.user_data['provider'] = update.message.text
    logger.info(f"User {user.id} entered provider: {update.message.text}")
    
    await update.message.reply_text("What was the course name?")
    return COURSE

async def course(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store course and ask for project details."""
    user = update.effective_user
    context.user_data['course'] = update.message.text
    logger.info(f"User {user.id} entered course: {update.message.text}")
    
    await update.message.reply_text("Did you complete any project? Please describe:")
    return PROJECT

async def project(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store project and ask for certificate image."""
    user = update.effective_user
    context.user_data['project'] = update.message.text
    logger.info(f"User {user.id} entered project details")
    
    await update.message.reply_text("Please send your certificate image:")
    return CERTIFICATE

async def certificate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store certificate image name and save all data to MongoDB."""
    user = update.effective_user
    try:
        # Get the image file
        photo = update.message.photo[-1]
        
        # Generate image filename without saving the actual file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = f"{user.id}_{timestamp}_{context.user_data['achievement'].lower().replace(' ', '_')}.jpg"
        
        # Prepare data for MongoDB
        achievement_data = {
            'user_id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'achievement': context.user_data['achievement'],
            'description': context.user_data['description'],
            'duration': context.user_data['duration'],
            'provider': context.user_data['provider'],
            'course': context.user_data['course'],
            'project': context.user_data['project'],
            'certificateImage': image_filename,
            'created_at': datetime.now()
        }
        
        # Insert into MongoDB
        result = collection.insert_one(achievement_data)
        logger.info(f"Achievement saved for user {user.id} with ID: {result.inserted_id}")
        
        await update.message.reply_text(
            "Achievement recorded successfully! Here's what I saved:\n\n"
            f"Achievement: {context.user_data['achievement']}\n"
            f"Description: {context.user_data['description']}\n"
            f"Duration: {context.user_data['duration']}\n"
            f"Provider: {context.user_data['provider']}\n"
            f"Course: {context.user_data['course']}\n"
            f"Project: {context.user_data['project']}\n"
            f"Certificate Image: {image_filename}\n\n"
            "To record another achievement, use /start"
        )
        
        # Clear user data
        context.user_data.clear()
        
        return ConversationHandler.END
        
    except Exception as e:
        logger.error(f"Error saving achievement for user {user.id}: {str(e)}")
        await update.message.reply_text(
            "Sorry, there was an error saving your achievement. Please try again later."
        )
        return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel the conversation."""
    user = update.effective_user
    logger.info(f"User {user.id} canceled the operation")
    
    await update.message.reply_text(
        'Operation cancelled. Type /start to begin again.',
        reply_markup=ReplyKeyboardRemove()
    )
    context.user_data.clear()
    return ConversationHandler.END

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors in the conversation."""
    logger.error(f"Update {update} caused error {context.error}")
    try:
        await update.message.reply_text(
            "Sorry, an error occurred. Please try again using /start"
        )
    except:
        logger.error("Could not send error message to user")

def main() -> None:
    """Run the bot."""
    try:
        # Create the Application
        application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

        # Add conversation handler
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                ACHIEVEMENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, achievement)],
                DESCRIPTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, description)],
                DURATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, duration)],
                PROVIDER: [MessageHandler(filters.TEXT & ~filters.COMMAND, provider)],
                COURSE: [MessageHandler(filters.TEXT & ~filters.COMMAND, course)],
                PROJECT: [MessageHandler(filters.TEXT & ~filters.COMMAND, project)],
                CERTIFICATE: [MessageHandler(filters.PHOTO, certificate)],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
        )

        application.add_handler(conv_handler)
        
        # Add error handler
        application.add_error_handler(error_handler)

        # Start the bot
        logger.info("Starting bot...")
        application.run_polling()
        
    except Exception as e:
        logger.error(f"Error starting bot: {str(e)}")
        raise

if __name__ == '__main__':
    main()