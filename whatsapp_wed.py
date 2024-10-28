import pywhatkit as pwk
from datetime import time
from whatsapp_common import setup_logging, get_random_time, GROUP_ID
import logging

SCHEDULES = {
    'Wednesday': {
        'message': "Hey, just a reminder, that we're meeting at Lara's later today",
        'time_range': (time(10, 0), time(11, 0))
    },
    'Wednesday_evening': {
        'message': "thank for coming everybody",
        'time_range': (time(21, 40), time(22, 15))
    }
}

def schedule_wednesday_messages():
    """Schedule both Wednesday messages."""
    for schedule_key, schedule_data in SCHEDULES.items():
        message = schedule_data['message']
        start_time, end_time = schedule_data['time_range']
        
        logging.info(f"Processing schedule for {schedule_key}")
        
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
            
            logging.info(f"Successfully scheduled message for {schedule_key} at {hour:02d}:{minute:02d}")
            
        except Exception as e:
            logging.error(f"Error scheduling message: {str(e)}")

if __name__ == "__main__":
    setup_logging("wed")
    logging.info("Starting Wednesday WhatsApp scheduler")
    schedule_wednesday_messages()
    logging.info("Finished execution") 