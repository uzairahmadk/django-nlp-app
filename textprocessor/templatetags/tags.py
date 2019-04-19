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

@register.filter(name='ListCounter')
def ListCounter(counting_list):
    #return total number of items of the list
    return len(counting_list)

@register.filter(name='DictCounter')
def DictCounter(counting_dict):
    #return total number of items of the dictionary
    counter = 0

    for key, value in counting_dict.items():
        counter = counter + 1

    return counter

@register.filter(name='ListDictCounter')
def ListDictCounter(counting_list_dict):
    #return total number of items of the dictionary inside a list
    counter = 0

    #unpacking the list
    for list_item in counting_list_dict:

        #unpacking the inner dictionary
        for key, value in list_item.items():
            counter = counter + 1

    return counter

@register.filter(name='ListElementReturn')
def ListElementReturn(list, index_number):
    return list[index_number]
