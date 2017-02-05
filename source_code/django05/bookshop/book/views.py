from django.http import HttpResponse
from django.views.generic import View
from django.template import loader
from django.core.urlresolvers import reverse



def index(request, name):
    template = loader.get_template('book/index.html')
    context = {
        'name': name,
    }
    return HttpResponse(template.render(context, request))


def list_books(request):
    return HttpResponse("<h1>List All Book</h1>")


def book_detail(request, category, book_id):
    url = reverse('book:book_detail', args=[category, book_id])
    return HttpResponse("Url: " + url)



class IndexView(View):

    def get(self, request):
        return HttpResponse("Hello world")

