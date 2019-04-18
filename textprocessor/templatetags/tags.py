from django import template
from random import shuffle
from textprocessor.choices import *

register = template.Library()

@register.filter(name='BoxColor')
def BoxColor(choice_name):
    #Scrambled and randomly send one value from the list
    options = box_options
    shuffle(options)
    return options[0]
