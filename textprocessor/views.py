from django.shortcuts import render
from django.views.generic import View
from textprocessor.forms import TextProcessingForm
from textprocessor.processingscripts.texttagprocess import TextTagProcess
from textprocessor.processingscripts.textnounprocess import TextNounProcess

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
        results = {}
        choices = []

        if form.is_valid():
            text = form.cleaned_data['text']

            choices.append('Tags')
            results['Tags'] = self.processor_class.text_tag(text)


            return render(request, 'tag_processor/result-view.html', {'results': results, 'choices': choices, 'error': self.form_error})

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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        results = {}
        choices = []

        if form.is_valid():
            text = form.cleaned_data['text']

            choices.append('Nouns')
            results['Nouns'] = self.processor_class.text_noun(text)


            return render(request, 'noun_processor/result-view.html', {'results': results, 'choices': choices, 'error': self.form_error})

        else:
            self.form_error = True
            return render(request, 'noun_processor/result-view.html', {'error': self.form_error})
