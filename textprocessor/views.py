from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.cache import never_cache
from textprocessor.forms import TextProcessingForm
from textprocessor.processingscripts.texttagprocess import TextTagProcess
from textprocessor.processingscripts.textnounprocess import TextNounProcess
from textprocessor.processingscripts.textwordprocess import TextWordProcess
from textprocessor.processingscripts.textsentenceprocess import TextSentenceProcess
from textprocessor.processingscripts.generalclasses.general_text_processing import GeneralTextProcessing

# Create your views here.
class TagProcessorView(View):
    template_name = 'tag_processor/textform-view.html'
    form_class = TextProcessingForm
    context_object_name = 'text_form'
    initial = {'key': 'value'}
    processor_class = TextTagProcess()
    form_error = False

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        results = []

        if form.is_valid():
            text = form.cleaned_data['text']

            results.append(self.processor_class.text_tag(text))


            return render(request, 'tag_processor/result-view.html', {'results': results, 'error': self.form_error})

        else:
            self.form_error = True
            return render(request, 'tag_processor/result-view.html', {'error': self.form_error})


# Create your views here.
class NounProcessorView(View):
    template_name = 'noun_processor/textform-view.html'
    form_class = TextProcessingForm
    context_object_name = 'text_form'
    initial = {'key': 'value'}
    processor_class = TextNounProcess()
    form_error = False

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    @never_cache
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            results = self.processor_class.text_noun(text)

            return render(request, 'noun_processor/result-view.html', {'results': results, 'error': self.form_error})

        else:
            self.form_error = True
            return render(request, 'noun_processor/result-view.html', {'error': self.form_error})


# Create your views here.
class WordProcessorView(View):
    template_name = 'word_processor/textform-view.html'
    form_class = TextProcessingForm
    context_object_name = 'text_form'
    initial = {'key': 'value'}
    processor_class = TextWordProcess()
    form_error = False

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            results = self.processor_class.text_word(text)

            return render(request, 'word_processor/result-view.html', {'results': results, 'error': self.form_error})

        else:
            self.form_error = True
            return render(request, 'word_processor/result-view.html', {'error': self.form_error})


# Create your views here.
class SentenceProcessorView(View):
    template_name = 'sentence_processor/textform-view.html'
    form_class = TextProcessingForm
    context_object_name = 'text_form'
    initial = {'key': 'value'}
    processor_class = TextSentenceProcess()
    general_processor_class = GeneralTextProcessing()
    form_error = False

    def total_sentiment(self, dict, index_number):
        return self.general_processor_class.total_text_vibe(dict, index_number)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        total_vibe = []

        if form.is_valid():
            text = form.cleaned_data['text']
            results = self.processor_class.text_sentence(text)

            #find total sentimental vibe of the entire text
            total_vibe.append(self.total_sentiment(results, 2))

            #find total subjectivity vibe of the entire text
            total_vibe.append(self.total_sentiment(results, 4))
            
            return render(request, 'sentence_processor/result-view.html', {'results': results, 'total_vibe': total_vibe, 'error': self.form_error})

        else:
            self.form_error = True
            return render(request, 'sentence_processor/result-view.html', {'error': self.form_error})
