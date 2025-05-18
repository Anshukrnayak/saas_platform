from django.http import HttpResponse

def home_page_view(request):
   return HttpResponse('<h3> This is page of application </h3>')

# Prepare for production environment

# Deploy Django to Railway with docker containers



