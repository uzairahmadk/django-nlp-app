from textblob import TextBlob
from textprocessor.choices import *


class ResultCounter:

    def tag_abreviation_checker(self, abbr):

        detail_data = 'Nothing'

        for key, value in tag_details.items():
            if key == abbr:
                detail_data = value
                break
        return detail_data


class ResultCleaner:

    def first_bracket_first_parenthesis_remover(self, text):
        return text.replace("(", "")

    def first_bracket_second_parenthesis_remover(self, text):
        return text.replace(")", "")

    def single_quote_remover(self, text):
        return text.replace("'", "")

    def space_remover(self, text):
        return text.replace(" ", "")

    def tag_comma_splitter(self, text, index_value):
        return text.split(',')[index_value]


class TextProcess:

    result_counter = ResultCounter()
    text_cleaner = ResultCleaner()
    return_result = []

    def text_tag(self, text):
        blob = TextBlob(text)
        blob = blob.tags

        for data in blob:

            ##remove the first bracket first parenthesis
            data = self.text_cleaner.first_bracket_first_parenthesis_remover(str(data))

            ##remove the first bracket second parenthesis
            data = self.text_cleaner.first_bracket_second_parenthesis_remover(str(data))

            ##remove the single quote from string
            data = self.text_cleaner.single_quote_remover(str(data))

            ##spliting comma from the string
            first_value = self.text_cleaner.tag_comma_splitter(str(data), 0)
            last_value = self.text_cleaner.tag_comma_splitter(str(data), 1)

            ##detect abreviation
            last_value = self.result_counter.tag_abreviation_checker(self.text_cleaner.space_remover(last_value))

            data = first_value + ' ' + last_value

            self.return_result.append(data)

        return self.return_result

    def text_noun(text):
        blob = TextBlob(text)
        return blob.noun_phrases

    def text_word(text):
        blob = TextBlob(text)
        return blob.words

    def text_sentence(text):
        blob = TextBlob(text)
        return blob.sentences
