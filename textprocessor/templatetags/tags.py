from django import template
from random import shuffle
from textprocessor.choices import *

register = template.Library()

@register.filter
def AppURLChecker(page_url, finder_url):
    if finder_url in page_url:
        return True
    else:
        return False

@register.filter(name='BoxColor')
def BoxColor(choice_name):
    #Scrambled and randomly send one value from the list
    options = box_options
    shuffle(options)
    return options[0]

@register.filter(name='TagSplitter')
def TagSplitter(tag_data, index_number):
    #split the tag data and return the desired index value
    tag_data = tag_data.split(' ')[index_number]
    return tag_data

@register.filter(name='TotalNumber')
def TotalNumber(result_dict, key_value):
    #counting the total number of items based on key
    counter = 0
    for key, value in result_dict.items():
        if key == key_value:
            for sub_value in value:
                counter = counter + 1

    return counter
