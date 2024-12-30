
from django.shortcuts import render

# Create your views here.
'''
def index_page(request):
  return render(request, 'myapp1/index.html', {})
'''

def home_page(request):
  return render(request, 'myapp1/home.html')