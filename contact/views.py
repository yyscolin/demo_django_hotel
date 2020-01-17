from django.shortcuts import render, redirect
from .forms import Message_Form

def contact(request):
  if request.method == 'POST':
    form = Message_Form(request.POST)
    if form.is_valid():
      form.save()
      return render(request, 'contact_completed.html', {'form': form})
  else:
    form = Message_Form()
  
  return render(request, 'contact.html', {'form': form})