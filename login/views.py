
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render

def view_name(request):
  return render(request, 'home.html', {})
