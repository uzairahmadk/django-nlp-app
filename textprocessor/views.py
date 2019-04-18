from django.shortcuts import render
from django.views.generic import View
from textprocessor.forms import TextProcessingForm
from textprocessor.textprocess import TextProcess
from textprocessor.choices import *

# Create your views here.
class HomePageView(View):
    template_name = 'textform-view.html'
    form_class = TextProcessingForm
    context_object_name = 'text_form'
    initial = {'key': 'value'}
    processor_class = TextProcess
    form_error = False

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        results = {}
        choices = []

        if form.is_valid():
            text = form.cleaned_data['text']
            feature_choice = form.cleaned_data['feature_choice']

            for feature in feature_choice:

                ##Text tags processing
                if feature == 'Tags':
                    choices.append('Tags')
                    results['Tags'] = self.processor_class.text_tag(text)
                    #results.append(self.processor_class.text_tag(text))
                elif feature == 'Nouns':
                    choices.append('Nouns')
                    results['Nouns'] = self.processor_class.text_noun(text)
                    #results.append(self.processor_class.text_noun(text))
                elif feature == 'Words':
                    choices.append('Words')
                    results['Words'] = self.processor_class.text_word(text)
                    #results.append(self.processor_class.text_word(text))
                else:
                    choices.append('Sentences')
                    results['Sentences'] = self.processor_class.text_sentence(text)
                    #results.append(self.processor_class.text_sentence(text))


            return render(request, 'result-view.html', {'results': results, 'choices': choices, 'box_color': box_options, 'error': self.form_error})

        else:
            self.form_error = True
            return render(request, 'result-view.html', {'error': self.form_error})
