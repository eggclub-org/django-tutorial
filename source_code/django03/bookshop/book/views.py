from django.http import HttpResponse
from django.views.generic import View
from django.template import loader


def index(request):
    template = loader.get_template('book/index.html')
    context = {
        'name': "Boss",
    }
    return HttpResponse(template.render(context, request))


class IndexView(View):

    def get(self, request):
        return HttpResponse("Hello world")

