from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    '''
        This is the landing page of the website.
    '''

    template = loader.get_template("sentiment/index.html")
    context = {}

    return HttpResponse(template.render(context, request))