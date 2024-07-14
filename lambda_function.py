import json
from lambda_logger import get_logger

from clients import holiday_client

logger = get_logger()


def lambda_handler(event, context):
    print(event)
    logger.info(f"lambda_handler initiated {event}")

    try:
        event_handler = extract_event_handler(event)

        log_message = json.dumps({"Event received": {event_handler}})
        logger.info(log_message)

    except Exception as e:
        error_message = json.dumps({"Error event handler not provided": str(e)})
        logger.exception(error_message, exc_info=True)
        raise Exception

    if event_handler == "GET_Holidays":
        try:
            return holiday_client.is_today_a_holiday()
        except Exception as error:
            error_message = json.dumps(
                {"The GET_Holidays validation error occured": error}
            )
            logger.exception(error_message, exc_info=True)
            raise Exception
    ### TODO: To test the full experience please say test full experience, to test the lambda holiday say test holiday.
    elif event_handler == "PUT_Holidays":
        try:
            return holiday_client.force_today_as_holiday()
        except Exception as error:
            error_message = json.dumps(
                {"The PUT_Holidays validation error occured": error}
            )
            logger.exception(error_message, exc_info=True)
            raise Exception

    ### TODO: Also need to find sources or API's that are available publically to GET info for lex > lambda validation such as an address

    ### TODO: When building the flow PLEASE stay customer focussed and inform the customer where they are and why we are collecting the information.

    ### TODO: Bonus


def extract_event_handler(event):
    """Extracts the eventHandler from the given event."""
    try:
        event_data = json.loads(event)
        event_handler = event_data["Parameters"]["eventHandler"]
        return event_handler
    except (KeyError, json.JSONDecodeError) as e:
        try:
            return extact_lex_event(event)
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Error extracting eventHandler: {e}")
            return None


def extact_lex_event(event):
    try:
        lambda_intent = event["sessionState"]["intent"]["name"]
        return lambda_intent
    except (KeyError, json.JSONDecodeError) as e:
        print(f"Error extracting eventHandler: {e}")
        return None

    lex_event = {
        "sessionId": "d11ce775-ca4b-41de-b889-87c6591dbf40",
        "requestAttributes": {
            "x-amz-lex:accept-content-types": "PlainText,SSML",
            "x-amz-lex:channels:platform": "Connect",
        },
        "inputTranscript": "food stamps",
        "rawInputTranscript": "food stamps",
        "interpretations": [
            {
                "nluConfidence": 1.0,
                "intent": {
                    "name": "BIAA_Eligibility_Type",
                    "slots": {
                        "biaaEType": {
                            "shape": "Scalar",
                            "value": {
                                "originalValue": "food stamps",
                                "resolvedValues": ["Food stamps"],
                                "interpretedValue": "Food stamps",
                            },
                        }
                    },
                    "state": "InProgress",
                    "confirmationState": "None",
                },
                "interpretationSource": "Lex",
            },
            {
                "intent": {
                    "name": "FallbackIntent",
                    "slots": {},
                    "state": "InProgress",
                    "confirmationState": "None",
                },
                "interpretationSource": "Lex",
            },
            {
                "nluConfidence": 0.44,
                "intent": {
                    "name": "BIAA_Eligibility",
                    "slots": {"Eligibility": None},
                    "state": "InProgress",
                    "confirmationState": "None",
                },
                "interpretationSource": "Lex",
            },
            {
                "nluConfidence": 0.42,
                "intent": {
                    "name": "BIAA",
                    "slots": {
                        "BIAASlot": {
                            "shape": "Scalar",
                            "value": {
                                "originalValue": "food stamps",
                                "resolvedValues": [],
                            },
                        }
                    },
                    "state": "InProgress",
                    "confirmationState": "None",
                },
                "interpretationSource": "Lex",
            },
        ],
        "bot": {
            "name": "connect_demo",
            "version": "2",
            "localeId": "en_US",
            "id": "5NKCG7UK79",
            "aliasId": "LZ1SZRHAQU",
            "aliasName": "connect_demo",
        },
        "responseContentType": "text/plain; charset=utf-8",
        "sessionState": {
            "sessionAttributes": {},
            "intent": {
                "name": "BIAA_Eligibility_Type",
                "slots": {
                    "biaaEType": {
                        "shape": "Scalar",
                        "value": {
                            "originalValue": "food stamps",
                            "resolvedValues": ["Food stamps"],
                            "interpretedValue": "Food stamps",
                        },
                    }
                },
                "state": "InProgress",
                "confirmationState": "None",
            },
            "originatingRequestId": "26f10138-8657-4b7d-baec-8801066dabf8",
        },
        "messageVersion": "1.0",
        "invocationSource": "DialogCodeHook",
        "transcriptions": [
            {
                "resolvedContext": {"intent": "BIAA_Eligibility_Type"},
                "transcriptionConfidence": 0.88,
                "transcription": "food stamps",
                "rawTranscription": "food stamps",
                "resolvedSlots": {
                    "biaaEType": {
                        "shape": "Scalar",
                        "value": {
                            "originalValue": "food stamps",
                            "resolvedValues": ["Food stamps"],
                        },
                    }
                },
            },
            {
                "resolvedContext": {},
                "transcriptionConfidence": 0.76,
                "transcription": "stamps",
                "rawTranscription": "stamps",
                "resolvedSlots": {},
            },
            {
                "resolvedContext": {},
                "transcriptionConfidence": 0.66,
                "transcription": "no stamps",
                "rawTranscription": "no stamps",
                "resolvedSlots": {},
            },
        ],
        "inputMode": "Speech",
    }
