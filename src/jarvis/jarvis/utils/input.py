import jarvis
from jarvis.core.console import ConsoleManager

console_manager = ConsoleManager()


def validate_digits_input(message, values_range=None):
    """
    Checks users input to be only numbers else it will be in infinite loop for a right value.
    Extra parameter 'values_range' checks the input to be between a range.
    """
    input_number = None
    while True:
        jarvis.output_engine.assistant_response(message)
        user_input = jarvis.input_engine.recognize_input(already_activated=True)
        try:
            input_number = int(user_input)
        except ValueError:
            continue

        if values_range:
            min_value = values_range[0]
            max_value = values_range[1]
            if not min_value <= input_number <= max_value:
                jarvis.output_engine.assistant_response\
                    ("Please give a number higher/equal than {0} and smaller/equal than {1}".format(min_value, max_value))
                raise ValueError
            else:
                break
    return input_number


def check_input_to_continue(message=''):
    positive_answers = ['yes', 'y', 'sure', 'yeah']
    if message:
        console_manager.console_output(message + ' (y/n): ', refresh_console=False)
    return jarvis.input_engine.recognize_input(already_activated=True) in positive_answers


def validate_input_with_choices(available_choices):
    user_input = jarvis.input_engine.recognize_input(already_activated=True)
    while not user_input in available_choices:
        jarvis.output_engine.assistant_response('Please select on of the values: {0}'.format(available_choices))
        user_input = jarvis.input_engine.recognize_input(already_activated=True)
    return user_input

