from django.shortcuts import render
from django.views.generic import View
from textprocessor.forms import TextProcessingForm

# Create your views here.
class HomePageView(View):
    template_name = 'textform-view.html'
    form_class = TextProcessingForm
    context_object_name = 'text_form'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})
