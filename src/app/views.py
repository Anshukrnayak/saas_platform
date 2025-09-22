from django.http import HttpResponse
from django.shortcuts import  render
from .models import VisitModel

def home_page_view(request):
    data=VisitModel.objects.create()

    data=VisitModel.objects.all().count()
    print(f'page count : {data} ')
    return render(request,template_name='index.html',context={'page_count':data})

