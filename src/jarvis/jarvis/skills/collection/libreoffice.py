import subprocess

from jarvis.skills.skill import AssistantSkill


class LibreofficeSkills(AssistantSkill):

    @classmethod
    def open_libreoffice_calc(cls, **kwargs):
        """
        Opens libreoffice_suite_skills calc application.
        """
        cls._open_libreoffice_app('calc')

    @classmethod
    def open_libreoffice_impress(cls, **kwargs):
        """
        Opens libreoffice_suite_skills impress application.
        """
        cls._open_libreoffice_app('impress')

    @classmethod
    def open_libreoffice_writer(cls, **kwargs):
        """
        Opens libreoffice_suite_skills writer application.
        """
        cls._open_libreoffice_app('writer')

    @classmethod
    def _open_libreoffice_app(cls, app):
        app_arg = '-' + app
        subprocess.Popen(['libreoffice', app_arg], stdout=subprocess.PIPE, shell=False)
        cls.console('I opened a new' + app + ' document..')
