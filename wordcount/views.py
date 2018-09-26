from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddic = {}

    for word in wordlist:
        if word in worddic:
            #Increase
            worddic[word] += 1
        else:
            #add to the dic
            worddic[word] = 1

    sortedwords = sorted(worddic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html')

def gestores(request):
    return render(request, './output/02.Gestores.html')
