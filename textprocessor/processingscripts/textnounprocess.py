from textblob import TextBlob
from textprocessor.processingscripts.generalclasses.resultcleaner import ResultCleaner
from textprocessor.choices import *


class TextNounProcess:

    result_counter = ResultCounter()
    text_cleaner = ResultCleaner()
    return_result = []

    def text_noun(text):
        blob = TextBlob(text)
        return blob.noun_phrases
