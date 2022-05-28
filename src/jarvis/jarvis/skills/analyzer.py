import logging
from jarvis.utils.mapping import math_symbols_mapping
from jarvis.utils.mongoDB import db


class SkillAnalyzer:
    def __init__(self, weight_measure, similarity_measure, args, sensitivity):
        self.logger = logging
        self.weight_measure = weight_measure
        self.similarity_measure = similarity_measure
        self.args = args
        self.vectorizer = self._create_vectorizer()
        self.analyzer_sensitivity = sensitivity

    @property
    def skills(self):
        return db.get_documents(collection='control_skills')\
               + db.get_documents(collection='enabled_basic_skills')\
               + db.get_documents(collection='learned_skills')

    @property
    def tags(self):
        tags_list = []
        for skill in self.skills:
            tags_list.append(skill['tags'].split(','))
        return [','.join(tag) for tag in tags_list]

    def extract(self, user_transcript):

        train_tdm = self._train_model()
        user_transcript_with_replaced_math_symbols = self._replace_math_symbols_with_words(user_transcript)

        test_tdm = self.vectorizer.transform([user_transcript_with_replaced_math_symbols])

        similarities = self.similarity_measure(train_tdm, test_tdm)  # Calculate similarities

        skill_index = similarities.argsort(axis=None)[-1]  # Extract the most similar skill
        if similarities[skill_index] > self.analyzer_sensitivity:
            skill_key = [skill for skill in enumerate(self.skills) if skill[0] == skill_index][0][1]
            return skill_key
        else:
            self.logger.debug('Not extracted skills from user voice transcript')
            return None

    def _replace_math_symbols_with_words(self, transcript):
        replaced_transcript = ''
        for word in transcript.split():
            if word in math_symbols_mapping.values():
                for key, value in math_symbols_mapping.items():
                    if value == word:
                        replaced_transcript += ' ' + key
            else:
                replaced_transcript += ' ' + word
        return replaced_transcript

    def _create_vectorizer(self):
        """
        Create vectorizer.
        """
        return self.weight_measure(**self.args)

    def _train_model(self):
        """
        Create/train the model.
        """
        return self.vectorizer.fit_transform(self.tags)
