from textblob import TextBlob
from textprocessor.processingscripts.generalclasses.resultcleaner import ResultCleaner
from textprocessor.choices import *


class TextWordProcess:

    text_cleaner = ResultCleaner()
    return_result = []

    def text_word(text):
        blob = TextBlob(text)
        return blob.words