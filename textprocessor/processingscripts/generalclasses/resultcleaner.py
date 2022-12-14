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

    def lower_case(self, string):
        return string.lower()

    def semicolon_splitter(self, text, index_value):
        return text.split(';')[index_value]

    def tuple_extractor(self, rcv_tuple, index_number):
        return rcv_tuple[index_number]
