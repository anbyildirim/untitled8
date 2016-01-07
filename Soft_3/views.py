from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import render_to_response
from forms import Teacher

def index(request):
    if request.method=="GET":
        teacher= Teacher
        return render_to_response("base_html.html",{"types":teacher})
    #return HttpResponse("Hello, world. You're at the polls index.")


def search(request):
    if 'q' in request.GET:
        message = 'You searched for : %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
'''

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
        {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.') '''