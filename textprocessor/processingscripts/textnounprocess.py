from textblob import TextBlob
from textprocessor.processingscripts.generalclasses.resultcleaner import ResultCleaner
from textprocessor.choices import *


class TextNounProcess:

    text_cleaner = ResultCleaner()
    return_result = []

    def text_noun(self, text):
        blob = TextBlob(text)
        return blob.noun_phrases
