import re

from jarvis.skills.skill import AssistantSkill
from jarvis.utils.mongoDB import db

header = """
-----------------------------------------------------------------------------------------------
- History                                                                                     -
-----------------------------------------------------------------------------------------------
* Note: The default limit is 3. Change the limit by adding a number e.g show me user history 10.

"""

response_base = """
* User Transcript: {0}
* Response: {1}
* Executed Skill: {2}
-----------------------------------------------------------------------------------------------"""


class HistorySkills(AssistantSkill):
    default_limit = 3

    @classmethod
    def show_history_log(cls, voice_transcript, skill):
        """
        This method cls.consoles user commands history & assistant responses.

        """

        limit = cls._extract_history_limit(voice_transcript, skill)
        limit = limit if limit else cls.default_limit
        documents = db.get_documents(collection='history', limit=limit)
        response = cls._create_response(documents)
        cls.console(response)

    @classmethod
    def _create_response(cls, documents):
        response = ''
        try:
            for document in documents:
                response += response_base.format(document.get('user_transcript', '--'),
                                                 document.get('response', '--'),
                                                 document.get('executed_skill').get('skill').get('name') if
                                                 document.get('executed_skill') else '--'
                                                 )
        except Exception as e:
            cls.console(error_log=e)
        finally:
            from jarvis.utils import input, console
            return header + response

    @classmethod
    def _extract_history_limit(cls, voice_transcript, skill):
        tags = cls.extract_tags(voice_transcript, skill['tags'])
        only_number_regex = '([0-9]+$)'
        for tag in tags:
            reg_ex = re.search(tag + ' ' + only_number_regex, voice_transcript)
            if reg_ex:
                limit = int(reg_ex.group(1))
                return limit
