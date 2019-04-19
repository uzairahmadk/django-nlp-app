from textblob import TextBlob
from textblob.blob import Word
from textprocessor.processingscripts.generalclasses.resultcleaner import ResultCleaner
from textprocessor.choices import *


class TextWordProcess:

    text_cleaner = ResultCleaner()
    return_result = {}

    def text_weight(self, unique_word, all_word):

        for value in unique_word:
            self.return_result[value] = all_word.count(value)

        return self.return_result

    def text_word(self, text):
        blob = TextBlob(text)

        unique_word = []
        all_word = []

        for data in blob.words:

            #make all words lower case
            data = self.text_cleaner.lower_case(data)

            all_word.append(data)

            if data in unique_word:
                pass
            else:
                unique_word.append(data)

        return self.text_weight(unique_word, all_word)
