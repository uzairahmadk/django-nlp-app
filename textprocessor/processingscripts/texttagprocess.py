from textblob import TextBlob
from textprocessor.processingscripts.generalclasses.resultcleaner import ResultCleaner
from textprocessor.choices import *


class ResultCounter:

    def tag_abreviation_checker(self, abbr):

        detail_data = 'Nothing'

        for key, value in tag_details.items():
            if key == abbr:
                detail_data = value
                break
        return detail_data


class TextTagProcess:

    result_counter = ResultCounter()
    text_cleaner = ResultCleaner()
    return_result = []
    result_dict = {}

    def organizing_results(self, key_data):
        temp_value_list = []
        index_counter = 0

        for key in key_data:
            self.result_dict[key] = []
            for value in self.return_result:
                if key in value:
                    temp_value_list.append(value)

            self.result_dict[key] = temp_value_list
            temp_value_list = []

        return self.result_dict

    def text_tag(self, text):
        key_data = []
        value_data = []
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

            #remove space from the last value
            last_value = self.text_cleaner.space_remover(last_value)

            ##detect abreviation
            last_value = self.result_counter.tag_abreviation_checker(last_value)

            #self.result_dict[last_value] = first_value

            key_data.append(last_value)

            #value_data.append(first_value)

            ##concatanage strings
            data = first_value + ' ' + last_value

            self.return_result.append(data)

        final_dict = self.organizing_results(key_data)

        #return self.return_result

        #return self.result_dict

        return final_dict
