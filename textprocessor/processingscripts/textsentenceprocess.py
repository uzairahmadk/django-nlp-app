from textblob import TextBlob
from textblob.blob import Sentence
from collections import defaultdict
from textprocessor.processingscripts.generalclasses.resultcleaner import ResultCleaner
from textprocessor.processingscripts.generalclasses.general_text_processing import GeneralTextProcessing
from textprocessor.choices import *


class TextSentenceProcess:

    text_cleaner = ResultCleaner()
    general_processor = GeneralTextProcessing()
    return_result = defaultdict(list)

    def sentence_sentiment(self):
        for key, value in self.return_result.items():
            sentiment = Sentence(key)

            #analysis the total sentimental score of the sentence
            sentimental_score = 'Polarity: ' + str(sentiment.sentiment[0]) + ' Subjectivity: ' + str(sentiment.sentiment[1])
            self.return_result[key].append(sentimental_score)

            #analysis the percentage of negativity, positivity and neutrality of the sentence
            npn_percentage = self.general_processor.npn_percentage_statement(sentiment.sentiment.polarity)
            self.return_result[key].append(npn_percentage)

            #analyze overall polarity of the sentence
            npn_overall = self.general_processor.npn_overall_statement(sentiment.sentiment.polarity)
            self.return_result[key].append(npn_overall)

            #analyze the percentage of Subjectivity and objectivity of the sentence
            so_percentage = self.general_processor.so_percentage_statement(sentiment.sentiment[1])
            self.return_result[key].append(so_percentage)

            #analyze overall subjectivity of the sentence
            so_overall = self.general_processor.so_overall_statement(sentiment.sentiment[1])
            self.return_result[key].append(so_overall)

            #self.return_result[key].append(str(sentiment.sentiment.polarity))
        return self.return_result

    def text_sentence(self, text):
        blob = TextBlob(text)
        normal_dict = {}

        for data in blob.sentences:
            #stringify the data
            data = str(data)

            #insert each sentence as a key
            self.return_result[data]

        #analysis sentiment of the sentence
        self.return_result = self.sentence_sentiment()

        for key, values in self.return_result.items():
            normal_dict[key] = self.return_result[key]

        return normal_dict
