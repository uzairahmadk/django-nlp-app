from textblob import TextBlob
from textprocessor.processingscripts.generalclasses.resultcleaner import ResultCleaner
from textprocessor.choices import *


class TextNounProcess:

    text_cleaner = ResultCleaner()
    return_result = {}

    def noun_weight(self, total_nouns, distinct_noun):

        for value in distinct_noun:
            self.return_result[value] = total_nouns.count(value)

        return self.return_result

    def text_noun(self, text):
        blob = TextBlob(text)
        noun_phases = blob.noun_phrases
        np_counts = blob.np_counts

        total_nouns = []
        distinct_noun = []

        for data in noun_phases:
            total_nouns.append(data)

        for data in np_counts:
            distinct_noun.append(data)

        return self.noun_weight(total_nouns, distinct_noun)
