from textblob import TextBlob
from textblob.blob import Word
from collections import defaultdict
from textprocessor.processingscripts.generalclasses.resultcleaner import ResultCleaner
from textprocessor.choices import *


class TextWordProcess:

    text_cleaner = ResultCleaner()
    return_result = defaultdict(list)

    def detect_language(self):
        for key, value in self.return_result.items():

            #as detect_language not worked with symbols and less than 3 chars
            if isinstance(key, str) and len(key) >= 3:
                word = Word(key)
                language = word.detect_language()
                self.return_result[key].append(language)
            else:
                self.return_result[key].append('Not found')

        return self.return_result

    def text_weight(self, unique_word, all_word):

        for value in unique_word:
            #self.return_result[value] = all_word.count(value)
            self.return_result[value].append(all_word.count(value))

        return self.return_result

    def text_word(self, text):
        blob = TextBlob(text)

        unique_word = []
        all_word = []
        normal_dict = {}

        for data in blob.words:

            #make all words lower case
            data = self.text_cleaner.lower_case(data)

            all_word.append(data)

            if data in unique_word:
                pass
            else:
                unique_word.append(data)

        #detect text Weight
        self.return_result = self.text_weight(unique_word, all_word)

        #detect text language
        self.return_result = self.detect_language()

        #normalize the defaultdict
        for key, values in self.return_result.items():
            normal_dict[key] = values

        return normal_dict
