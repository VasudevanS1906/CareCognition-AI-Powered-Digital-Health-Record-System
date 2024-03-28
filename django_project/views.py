from django.shortcuts import render, redirect, HttpResponse
from .models import Health
from .forms import HealthForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from .forms import InputForm
import requests
import json
import sqlite3
import pandas as pd  
from django.db.models import Count


# Create your views here.
def home(request):
  return render(request, 'login.html')

def homeindex(request):
  return render(request, 'index.html')

def home1(request):
  if request.method == 'POST':
    form = HealthForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse(b'Data added successfully!')  # redirect to a new URL
  else:
    form = HealthForm()
  return render(request, 'index1.html', {'form': form})


def home2(request):
  selected_language = request.session.get('language')
  form = None

  if request.method == 'POST':
      if 'language' in request.POST:
          # User has selected a language
          selected_language = request.POST['language']
          request.session['language'] = selected_language
      else:
          # User has submitted the product form
          form = HealthForm(request.POST, request.FILES, language=selected_language)
          if form.is_valid():
              form.save()
              #return render(request, 'success.html', {'message': 'Data added successfully!'})
              return HttpResponse(b'Data added successfully!')


  if not selected_language:
      # If no language is selected, show the language selection form
      return render(request, 'index2.html')

  # Render the product form with the selected language
  form = form or HealthForm(language=selected_language)
  return render(request, 'index2.html', {'form': form})

def home3(request):
  form = HealthForm()
  if request.method == 'POST':
      form = HealthForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return HttpResponse(b'Data added successfully!')  # redirect to a new URL
  else:
      form = InputForm()
  return render(request, 'index3.html', {'form': form})

def home4(request):
  selected_language = request.session.get('language')
  form = HealthForm()

  if request.method == 'POST':
      form = HealthForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return HttpResponse(b'Data added successfully!')  # redirect to a new URL
  else:
      form = InputForm()

  return render(request, 'index4.html', {'form': form})

@csrf_exempt
def perform_ocr(request):
  if request.method == 'POST':
      username = 'your username'
      api_password = 'your password here'
      ocr_api_url = 'https://www.ocrwebservice.com/restservices/processDocument?gettext=true'

      image_file = request.FILES['image']

      try:
          data = {
            'file': image_file
          }
          auth = (username, api_password)

          response = requests.post(ocr_api_url, files=data, auth=auth)

          if response.ok:
              recognized_text = response.text
              return JsonResponse({'recognized_text': recognized_text})
          else:
              return JsonResponse({'error': 'Failed to perform OCR'}, status=500)
      except requests.RequestException as e:
          return JsonResponse({'error': f'Error performing OCR: {e}'}, status=500)
  else:
      return JsonResponse({'error': 'Method not allowed'}, status=405)

def home5(request):
  form = HealthForm()
  if request.method == 'POST':
      form = HealthForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return HttpResponse(b'Data added successfully!')  # redirect to a new URL
  else:
      form = InputForm()
  return render(request, 'index5.html', {'form': form})

def home6(request):
  form = HealthForm()
  if request.method == 'POST':
      form = HealthForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return HttpResponse(b'Data added successfully!')  # redirect to a new URL
  else:
      form = InputForm()
  return render(request, 'index6.html', {'form': form})
  #return render(request, 'index6.html')

def home7(request):
  emps = Health.objects.all()
  context = {
    'emps': emps
  }
  print(context)
  return render(request, 'index7.html',context)


def home8(request):
  # Get the age and total values from the database
  age_data = Health.objects.filter(age__in=[25, 36]).values('age').annotate(total=Count('age')).order_by('age')
  sex_data = Health.objects.values('sex').annotate(total=Count('sex'))
  # Prepare the data for the charts
  ages = [data['age'] for data in age_data]
  totals = [data['total'] for data in age_data]
  sexes = [data['sex'] for data in sex_data]
  sex_totals = [data['total'] for data in sex_data]
  # Render the template with the data
  return render(request, 'index8.html', {
    'ages': ages,
    'totals': totals,
    'sexes': sexes,
    'sex_totals': sex_totals,
  })


def age_chart(request):
  # Filtering the Health records for ages 25 and 36
  age_data = Health.objects.filter(age__in=[25, 36]).values('age').annotate(total=Count('age')).order_by('age')

  # Preparing data for the chart
  ages = [data['age'] for data in age_data]
  totals = [data['total'] for data in age_data]

  context = {
      'ages': ages,
      'totals': totals,
  }

  return render(request, 'index8.html', context)

def sex_chart(request):
  # Counting the number of occurrences of each sex
  sex_data = Health.objects.values('sex').annotate(total=Count('sex'))

  # Preparing data for the chart
  sexes = [data['sex'] for data in sex_data]
  totals = [data['total'] for data in sex_data]

  context = {
      'sexes': sexes,
      'totals': totals,
  }

  return render(request, 'index8.html', context)
    
