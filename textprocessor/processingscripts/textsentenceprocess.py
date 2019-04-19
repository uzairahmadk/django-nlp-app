from textblob import TextBlob
from textprocessor.processingscripts.generalclasses.resultcleaner import ResultCleaner
from textprocessor.choices import *


class TextWordProcess:

    text_cleaner = ResultCleaner()
    return_result = []

    def text_sentence(text):
        blob = TextBlob(text)
        return blob.sentences
