import pywhatkit as pwk
from datetime import time
from whatsapp_common import setup_logging, get_random_time, GROUP_ID
import logging

SCHEDULE = {
    'message': "have a great weekend everyone",
    'time_range': (time(13, 0), time(18, 0))
}

def schedule_friday_message():
    """Schedule Friday message."""
    message = SCHEDULE['message']
    start_time, end_time = SCHEDULE['time_range']
    
    logging.info("Processing Friday schedule")
    
    hour, minute = get_random_time(start_time, end_time)
    
    try:
        logging.info(f"Attempting to schedule message for {hour:02d}:{minute:02d}")
        
        pwk.sendwhatmsg_to_group(
            GROUP_ID,
            message,
            hour,
            minute,
            wait_time=15,
        )
        
        logging.info(f"Successfully scheduled message for Friday at {hour:02d}:{minute:02d}")
        
    except Exception as e:
        logging.error(f"Error scheduling message: {str(e)}")

if __name__ == "__main__":
    setup_logging("fri")
    logging.info("Starting Friday WhatsApp scheduler")
    schedule_friday_message()
    logging.info("Finished execution") 