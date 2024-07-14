import json
from datetime import date

import holidays

from lambda_logger import get_logger

logger = get_logger()


def is_today_a_holiday():
    try:
        today = date.today()
        us_holidays = holidays.US()
        return {"Holiday": today in us_holidays}
    
    except Exception as error:
        error_message = json.dumps({"The is_today_a_holiday error occured": error})
        logger.exception(error_message, exc_info=True)
        raise Exception 
    

def force_today_as_holiday():
    try:
        holiday = "01-01-2025"
        us_holidays = holidays.US()
        return {"Holiday": holiday in us_holidays, "HolidayName": us_holidays.get(holiday)}
    
    except Exception as error:
        error_message = json.dumps({"The force_today_as_holiday error occured": error})
        logger.exception(error_message, exc_info=True)
        raise Exception 
