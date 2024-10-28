import logging
import os
from datetime import time, datetime, timedelta
import random

# WhatsApp group name (exactly as it appears in WhatsApp)
GROUP_ID = "Test Group"  # The exact name of your WhatsApp group

def setup_logging(script_name: str):
    """Setup logging configuration with file cleanup."""
    log_file = f"whatsapp_{script_name}.log"
    
    if os.path.exists(log_file):
        open(log_file, 'w').close()
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def get_immediate_time():
    """Get time 2 minutes from now to allow proper loading."""
    future_time = datetime.now() + timedelta(minutes=2)
    return future_time.hour, future_time.minute

def get_random_time(start_time: time, end_time: time) -> tuple:
    """Generate a random time between start_time and end_time."""
    start_minutes = start_time.hour * 60 + start_time.minute
    end_minutes = end_time.hour * 60 + end_time.minute
    
    random_minutes = random.randint(start_minutes, end_minutes)
    hour = random_minutes // 60
    minute = random_minutes % 60
    
    logging.debug(f"Generated random time: {hour:02d}:{minute:02d}")
    return hour, minute