import pywhatkit as pwk
from datetime import datetime, time
import random
import logging
import os

# WhatsApp group ID (replace with your group ID)
GROUP_ID = "AB123CDEFGHijklmn"  # Example format, replace with your actual group ID

# Message schedules with time ranges
SCHEDULES = {
    'Monday': {
        'message': "Hello fam, wishing you a great week ahead",
        'time_range': (time(7, 0), time(8, 40))  # 7:00 AM to 8:40 AM
    },
    'Tuesday': {
        'message': "Hello friends, welcoming to our connect group meeting tomorrow",
        'time_range': (time(10, 0), time(13, 0))  # 10:00 AM to 1:00 PM
    },
    'Wednesday': {
        'message': "Hey, just a reminder, that we're meeting at Lara's later today",
        'time_range': (time(10, 0), time(11, 0))  # 10:00 AM to 11:00 AM
    },
    'Friday': {
        'message': "have a great weekend everyone",
        'time_range': (time(13, 0), time(18, 0))  # 1:00 PM to 6:00 PM
    }
}

def setup_logging():
    """Setup logging configuration with file cleanup."""
    # Define the log file name
    log_file = "whatsapp_scheduler.log"
    
    # If log file exists, clear its contents
    # The 'w' mode opens the file and truncates it to zero length
    if os.path.exists(log_file):
        open(log_file, 'w').close()
    
    # Configure the logging system with two handlers:
    # 1. FileHandler: Writes logs to the file
    # 2. StreamHandler: Prints logs to console
    logging.basicConfig(
        level=logging.INFO,  # Set minimum logging level
        format='%(asctime)s - %(levelname)s - %(message)s',  # Define log message format
        handlers=[
            logging.FileHandler(log_file),     # Handler for file output
            logging.StreamHandler()            # Handler for console output
        ]
    )

def get_random_time(start_time: time, end_time: time) -> tuple:
    """Generate a random time between start_time and end_time."""
    start_minutes = start_time.hour * 60 + start_time.minute
    end_minutes = end_time.hour * 60 + end_time.minute
    
    random_minutes = random.randint(start_minutes, end_minutes)
    hour = random_minutes // 60
    minute = random_minutes % 60
    
    # Log the generated time for debugging purposes
    logging.debug(f"Generated random time: {hour:02d}:{minute:02d}")
    return hour, minute

def schedule_today_messages():
    """Schedule messages for the current day if any."""
    # Get current day name (e.g., 'Monday', 'Tuesday', etc.)
    current_day = datetime.now().strftime('%A')
    logging.info(f"Checking schedule for {current_day}")
    
    # Check if there are any messages scheduled for today
    if current_day in SCHEDULES:
        # Extract schedule details for today
        schedule = SCHEDULES[current_day]
        message = schedule['message']
        start_time, end_time = schedule['time_range']
        
        # Log that we found a schedule and its time range
        logging.info(f"Found schedule for {current_day}")
        logging.debug(f"Time range: {start_time} - {end_time}")
        
        # Generate random send time within the specified range
        hour, minute = get_random_time(start_time, end_time)
        
        try:
            # Log attempt to schedule message
            logging.info(f"Attempting to schedule message for {hour:02d}:{minute:02d}")
            
            # Use pywhatkit to schedule the WhatsApp message
            pwk.sendwhatmsg_to_group(
                GROUP_ID,
                message,
                hour,
                minute,
                wait_time=15,  # Wait 15 seconds before sending
            )
            
            # Log successful scheduling
            logging.info(f"Successfully scheduled message for {current_day} at {hour:02d}:{minute:02d}")
            
        except Exception as e:
            # Log any errors that occur during scheduling
            logging.error(f"Error scheduling message: {str(e)}")
    else:
        # Log when no messages are scheduled for today
        logging.info(f"No messages scheduled for {current_day}")

if __name__ == "__main__":
    # Initialize logging when script is run directly
    setup_logging()
    
    # Log start of execution
    logging.info("Starting WhatsApp scheduler")
    
    # Run the main scheduling function
    schedule_today_messages()
    
    # Log end of execution
    logging.info("Finished execution") 