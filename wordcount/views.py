import operator

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddict = {}

    for word in wordlist:



        if word in worddict:
            #Increase by 1
            worddict[word] += 1
        else:
            worddict[word] = 1

    orderedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {"fulltext":fulltext, "count":len(wordlist), "worddict":orderedwords})

def about(request):

    return render(request, 'about.html')