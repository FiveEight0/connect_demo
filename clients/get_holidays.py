import json
from datetime import date
import holidays


def is_today_a_holiday():
    try:
        today = date.today()
        us_holidays = holidays.US()
        return {"Holiday": today in us_holidays}
    
    except Exception as error:
        return f"The holiday validation error occured {error}" 
