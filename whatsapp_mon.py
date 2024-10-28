import pywhatkit as pwk
from datetime import time
from whatsapp_common import setup_logging, get_immediate_time, GROUP_ID
import logging
import pyautogui
import time as tm

SCHEDULE = {
    'message': "Hello fam, wishing you a great week ahead",
    'time_range': (time(7, 0), time(8, 40))
}

def send_whatsapp_message(message: str):
    """Send WhatsApp message using direct input."""
    try:
        # Get screen size
        width, height = pyautogui.size()
        
        logging.info("Opening WhatsApp Web...")
        
        # Use pywhatkit's function but with modified parameters
        pwk.sendwhatmsg_to_group_instantly(
            GROUP_ID,
            message,
            *get_immediate_time(),
            tab_close=False,
            close_time=3,
            wait_time=30
        )
        
        # After WhatsApp Web loads, click in the middle of the screen
        tm.sleep(35)  # Wait for WhatsApp Web to load completely
        pyautogui.click(width/2, height/2)  # Click in the middle of screen
        
        # Type and send message
        pyautogui.typewrite(message)
        tm.sleep(2)
        pyautogui.press('enter')
        
        logging.info("Message sent successfully")
        
    except Exception as e:
        logging.error(f"Error sending message: {str(e)}")

def schedule_monday_message():
    """Schedule Monday message."""
    message = SCHEDULE['message']
    
    logging.info("Processing Monday schedule")
    logging.info("Please wait while WhatsApp Web loads...")
    
    try:
        send_whatsapp_message(message)
        logging.info("Message scheduled and sent successfully")
        
    except Exception as e:
        logging.error(f"Error scheduling message: {str(e)}")
        logging.info("Troubleshooting tips:")
        logging.info("1. Make sure WhatsApp Web is accessible")
        logging.info("2. Ensure you're logged into WhatsApp Web")
        logging.info("3. Verify the group name exists and is correct")
        logging.info("4. Try running the script again")

if __name__ == "__main__":
    setup_logging("mon")
    logging.info("Starting Monday WhatsApp scheduler")
    logging.info("Important: Please ensure you have WhatsApp Web access")
    schedule_monday_message()
    logging.info("Finished execution") 