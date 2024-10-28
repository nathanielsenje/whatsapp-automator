import pywhatkit as pwk
from datetime import time
from whatsapp_common import setup_logging, get_random_time, GROUP_ID
import logging

SCHEDULES = {
    'Monday': {
        'message': "Hello fam, wishing you a great week ahead",
        'time_range': (time(7, 0), time(8, 40))
    },
    'Tuesday': {
        'message': "Hello friends, welcoming to our connect group meeting tomorrow",
        'time_range': (time(10, 0), time(13, 0))
    }
}

def schedule_message(day: str):
    """Schedule message for the specified day if applicable."""
    if day in SCHEDULES:
        schedule = SCHEDULES[day]
        message = schedule['message']
        start_time, end_time = schedule['time_range']
        
        logging.info(f"Found schedule for {day}")
        
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
            
            logging.info(f"Successfully scheduled message for {day} at {hour:02d}:{minute:02d}")
            
        except Exception as e:
            logging.error(f"Error scheduling message: {str(e)}")
    else:
        logging.info(f"No messages scheduled for {day}")

if __name__ == "__main__":
    setup_logging("mon_tue")
    logging.info("Starting Monday-Tuesday WhatsApp scheduler")
    schedule_message('Monday')
    schedule_message('Tuesday')
    logging.info("Finished execution") 