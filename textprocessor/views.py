from django.shortcuts import render
from django.views.generic import View
from textblob import TextBlob
from textprocessor.forms import TextProcessingForm

# Create your views here.
class HomePageView(View):
    template_name = 'textform-view.html'
    form_class = TextProcessingForm
    context_object_name = 'text_form'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            blob = TextBlob(text)

            result = blob.tags

            return render(request, 'result-view.html', {'result': result})
