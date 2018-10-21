
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response


@sb.request_handler(can_handle_func=is_request_type("StopQuestioning"))
def answer_request_handler(handler_input):
    """
    Get keywords stored in persitent storage for session
    send keywords to MS Azure endpoint
    Speak response from Azure endpoint
    Ask if want to continue
    """
    # type: (HandlerInput) -> Response
    # Get keywords list

    # send keywords to api. save response to var

    # speak response

    # continue?
    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("Hello World", speech_text)).set_should_end_session(
        False).response
