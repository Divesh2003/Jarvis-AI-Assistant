import re
import time

from jarvis.skills.skill import AssistantSkill


class WordSkills(AssistantSkill):
    
    @classmethod
    def spell_a_word(cls, voice_transcript, skill, **kwargs):
        """
        Spell a words letter by letter.
        :param voice_transcript: string (e.g 'spell word animal')
        :param skill: dict (e.g
        """
        tags = cls.extract_tags(voice_transcript, skill['tags'])
        for tag in tags:
            reg_ex = re.search(tag + ' ([a-zA-Z]+)', voice_transcript)
            try:
                if reg_ex:
                    search_text = reg_ex.group(1)
                    for letter in search_text:
                        cls.response(letter)
                        time.sleep(2)
            except Exception as e:
                cls.console(error_log=e)
                cls.response("I can't spell the word")
