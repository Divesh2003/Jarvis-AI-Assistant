from jarvis.core.console import ConsoleManager
import jarvis


class AssistantSkill:
    """
    This class is the parent of all skill classes.
    """

    first_activation = True
    console_manager = ConsoleManager()

    @classmethod
    def console(cls, text='', debug_log=None, info_log=None, warn_log=None, error_log=None, refresh_console=True):
        """
        Prints the text only in console and update the console info.
        """

        cls.console_manager.console_output(text=text,
                                           debug_log=debug_log,
                                           info_log=info_log,
                                           warn_log=warn_log,
                                           error_log=error_log,
                                           refresh_console=refresh_console)

    @classmethod
    def response(cls, text, refresh_console=True):
        """
        The mode of the response depends on the output engine:
            - TTT Engine: The response is only in text
            - TTS Engine: The response is in voice and text
        """
        jarvis.output_engine.assistant_response(text, refresh_console=refresh_console)

    @classmethod
    def user_input(cls):
        user_input = jarvis.input_engine.recognize_input(already_activated=True)
        return user_input

    @classmethod
    def extract_tags(cls, voice_transcript, tags):
        """
        This method identifies the tags from the user transcript for a specific skill.

        e.x
        Let's that the user says "hi jarvis!".
        The skill analyzer will match it with enable_assistant skill which has tags 'hi, hello ..'
        This method will identify the that the enabled word was the 'hi' not the hello.

        :param voice_transcript: string
        :param tags: string
        :return: set
        """

        try:
            transcript_words = voice_transcript.split()
            tags = tags.split(',')
            return set(transcript_words).intersection(tags)
        except Exception as e:
            cls.console_manager.console_output(info_log='Failed to extract tags with message: {0}'.format(e))
            return set()
