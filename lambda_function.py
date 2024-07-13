import json
from lambda_logger import get_logger

from clients import get_holidays
from models.contact_flow_event import ContactFlowEvent

logger = get_logger()


def lambda_handler(event, context):
    logger.info("lambda_handler initiated")

    try:
        event_data = ContactFlowEvent(**event)
        event_handler = event_data.Parameters['eventHandler']
        
        log_message = json.dumps({"Event received": {event_handler}})
        logger.info(log_message)
        
    except Exception as e:
        error_message = json.dumps({"Error event handler not provided": str(e)})
        logger.exception(error_message, exc_info=True)
        raise

    if event_handler == "GET_Holidays":
        try:
            return get_holidays.is_today_a_holiday()
        except Exception as error:
                return f"The holiday validation error occured {error}" 
    
    ### TODO: Create logic to press a number to force a holiday using a manual date and adding a prompt in connect to use lex:  To test the full experience please say test full experience, to test the lambda holidy say test holiday.

    ### TODO: Also need to find sources or API's that are available publically to GET info for lex > lambda validation such as an address 

    ### TODO: When building the flow PLEASE stay customer focussed and inform the customer where they are and why we are collecting the information. 

    ### TODO: Bonus 

        
