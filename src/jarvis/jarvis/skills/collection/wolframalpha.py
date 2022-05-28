import wolframalpha

from jarvis.settings import WOLFRAMALPHA_API
from jarvis.skills.collection.internet import InternetSkills
from jarvis.skills.skill import AssistantSkill


class WolframSkills(AssistantSkill):
    
    @classmethod
    def call_wolframalpha(cls, voice_transcript, **kwargs):
        """
        Make a request in wolfram Alpha API and prints the response.
        """
        client = wolframalpha.Client(WOLFRAMALPHA_API['key'])
        if voice_transcript:
            try:
                if WOLFRAMALPHA_API['key']:
                    cls.console(info_log='Wolfarm APi call with query message: {0}'.format(voice_transcript))
                    cls.response("Wait a second, I search..")
                    res = client.query(voice_transcript)
                    wolfram_result = next(res.results).text
                    cls.console(debug_log='Successful response from Wolframalpha')
                    cls.response(wolfram_result)
                    return wolfram_result
                else:
                    cls.response("WolframAlpha API is not working.\n"
                          "You can get an API key from: https://developer.wolframalpha.com/portal/myapps/ ")
            except Exception as e:
                if InternetSkills.internet_availability():
                    # If there is an error but the internet connect is good, then the Wolfram API has problem
                    cls.console(error_log='There is no result from Wolfram API with error: {0}'.format(e))
                else:
                    cls.response('Sorry, but I could not find something')
