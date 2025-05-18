from django.http import HttpResponse

def home_page_view(request):
   return HttpResponse('<h3> This is page of application </h3>')

