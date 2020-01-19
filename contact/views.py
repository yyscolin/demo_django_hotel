from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Message_Form

def contact_view(request):
  form = Message_Form()
  return render(request, 'contact.html', {'form': form})

def contact_ajax(request):
  if request.method != 'POST' or not(request.is_ajax):
    return HttpResponse('Invalid Request Method', status=405)

  form = Message_Form(request.POST)
  if form.is_valid():
    form.save()
    return HttpResponse('Message Received')
  else:
    return HttpResponse('Invalid Form', status=400)