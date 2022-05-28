import subprocess
import logging
import time

from jarvis.skills.skill import AssistantSkill


class LinuxAppSkills(AssistantSkill):

    @classmethod
    def open_new_bash(cls, **kwargs):
        """
        Opens new bash terminal.
        """
        try:
            subprocess.Popen(['gnome-terminal'], stderr=subprocess.PIPE, shell=False).communicate()
        except Exception as e:
            cls.response("An error occurred, I can't open new bash terminal")
            logging.debug(e)

    @classmethod
    def open_note_app(cls, **kwargs):
        """
        Opens a note editor (gedit).
        """
        try:
            subprocess.Popen(['gedit'], stderr=subprocess.PIPE, shell=False).communicate()
        except FileNotFoundError:
            cls.response("You don't have installed the gedit")
            time.sleep(2)
            cls.response("Install gedit with the following command: 'sudo apt-get install gedit'")

    @classmethod
    def open_new_browser_window(cls, **kwargs):
        """
        Opens new browser window.
        """
        try:
            subprocess.Popen(['firefox'], stderr=subprocess.PIPE, shell=False).communicate()
        except Exception as e:
            cls.response("An error occurred, I can't open firefox")
            logging.debug(e)
