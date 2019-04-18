from textblob import TextBlob


class TextProcess:

    def text_tag(text):
        blob = TextBlob(text)
        return blob.tags

    def text_noun(text):
        blob = TextBlob(text)
        return blob.noun_phrases

    def text_word(text):
        blob = TextBlob(text)
        return blob.words

    def text_sentence(text):
        blob = TextBlob(text)
        return blob.sentences
