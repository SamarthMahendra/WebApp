from django.http import HttpResponse
from django.template import loader
from ai_models import modela
from django.views.decorators.csrf import csrf_exempt

def index(request):
    template= loader.get_template('index.html')
    return HttpResponse(template.render())

def about(request):
    template= loader.get_template('about.html')
    return HttpResponse(template.render())

def blog(request):
    template= loader.get_template('blog.html')
    return HttpResponse(template.render())

def contact(request):
    template= loader.get_template('contact.html')
    return HttpResponse(template.render())

def finance(request):
    template= loader.get_template('Finance.html')
    return HttpResponse(template.render())

def restaurant_review(request):
    template= loader.get_template('Restaurant review.html')
    return HttpResponse(template.render())

def services(request):
    template= loader.get_template('services.html')
    return HttpResponse(template.render())
def restaurant_review_search(request):
    template = loader.get_template('Restaurant review search.html')
    return HttpResponse(template.render())

@csrf_exempt
def run(request):
    s = request.POST['search_key']
    from ai_models import modela
    res = modela.model1(s)
    context = {
        'r':res
    }
    template = loader.get_template('restaurant review result.html')
    return HttpResponse(template.render(context,request))