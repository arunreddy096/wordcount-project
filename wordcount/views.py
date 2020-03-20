from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def count(request):
    a=request.GET['fulltext']
    c=a.split()
    d={}
    for i in c:
        if i in d:
            d[i] +=1
        else:
            d[i] = 1
    return render(request,'count.html',{'fulltext':a,'count':len(c),'wc':d.items()})