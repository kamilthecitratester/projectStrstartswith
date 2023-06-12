from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('waitwhat.html')
  return HttpResponse(template.render())

def news(request, question_id):
    return HttpResponse("You're looking at TEST %s." % question_id)



def rii(request):
  template = loader.get_template('template.html')
  context = {
    'tests': ['teSt2', 'Test', 'tEst3'],   
