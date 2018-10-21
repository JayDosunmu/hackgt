# -*- coding: utf-8 -*-

# This is a simple Hello World Alexa Skill, built using
# the decorators approach in skill builder.
import logging
import random

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

keyword_aggregation = [
  'What is your project?',
  'What languages are you using in your project?',
  'What are you trying to do?',
  'What is your current problem?'
]

context_driven = [
    'What technolgies does it incorporate?'
    'How are you using programming language in the project? ',
    'How are you implementing this framework?'
]

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch."""
    # type: (HandlerInput) -> Response
    speech_text = "Quack! What is it?"

    return handler_input.response_builder.speak(speech_text).ask(speech_text).response
    
@sb.request_handler(can_handle_func=is_request_type("StartQuestioning"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch."""
    # type: (HandlerInput) -> Response
    speech_text = "Okay. Let me ask you some questions."
    ask_text = keyword_aggregation[0]

    return handler_input.response_builder.speak(speech_text + ask_text).ask(ask_text).response


@sb.request_handler(can_handle_func=is_intent_name("HelloWorldIntent"))
def hello_world_intent_handler(handler_input):
    """Handler for Hello World Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "whats up"
    
    i = random.randint(0,lens[keyword_aggregation])

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard(keyword_aggregation[i], "I need help")).set_should_end_session(
        True).response


# @sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
# def help_intent_handler(handler_input):
#     """Handler for Help Intent."""
#     # type: (HandlerInput) -> Response
#     speech_text = "Whats Good!"

#     return handler_input.response_builder.speak(speech_text).ask(
#         speech_text).set_card(SimpleCard(
#             "Hello World", "Abele is awesome")).response


@sb.request_handler(
    can_handle_func=lambda handler_input:
        is_intent_name("AMAZON.CancelIntent")(handler_input) or
        is_intent_name("AMAZON.StopIntent")(handler_input))
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "Goodbye!"

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("Hello World", speech_text)).response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    # type: (HandlerInput) -> Response
    speech = (
        "The Hello World skill can't help you with that.  "
        "You can say hello!!")
    reprompt = "You can say hello!!"
    handler_input.response_builder.speak(speech).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    # type: (HandlerInput) -> Response
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    # type: (HandlerInput, Exception) -> Response
    logger.error(exception, exc_info=True)

    speech = "Bitch wtf!"
    handler_input.response_builder.speak(speech).ask(speech)

    return handler_input.response_builder.response


handler = sb.lambda_handler()
