# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from models import process, Report, datesofmonth
from forms import createReport
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.contrib.auth import login, authenticate
import datetime 
import json

# Create your views here.

def processlist(request):
    datadict = process.objects.all()
    if request.method == "POST":
        print "pst"
    return render(request, "home.html", {'form': datadict})

def repotadd(request):
    print "Ins"
    if request.method == "POST":
        form = createReport(request.POST)
        if form.is_valid():
            #print request.POST['CheckIn']
            #print request.POST['CheckOut']
            model_instance = form.save(commit=False)
            model_instance.save()
            print "saved"
    else:
        print "here"
        form = createReport()
    return render(request, "addcustomers.html", {'form': form})


def reportlist(request):
    reportsdate = Report.objects.values('DateofReport')
    daterange = datesofmonth.objects.exclude(weekday__in = reportsdate)
    missdates  = daterange.filter(weekday__range=(datetime.date.today().replace(day=1), datetime.date.today()))
    newdict = {}
    datadict =  Report.objects.all()
    datadict = serializers.serialize("json", datadict, )
    for fields in json.loads(datadict):
        #print fields['fields']
        if str(fields['fields']['DateofReport']) in newdict:
            newdict[str(fields['fields']['DateofReport'])].append(fields['fields'])
        else:
            newdict[str(fields['fields']['DateofReport'])] = [fields['fields']]
    newdict = sorted(newdict.items())
#     dates = Report.objects.values('DateofReport').distinct()
#     for date in dates:
#         print date['DateofReport']
#         reports = serializers.serialize("json", datadict.filter(DateofReport = date['DateofReport']))
#         print reports
#         for report in reports:
#             print report
#         if newdict.has_key(str(date['DateofReport'])):
#             newdict[str(date['DateofReport'])].append({str(report)})
#         else:
#             newdict[str(date['DateofReport'])] = {str(report)}
#     print newdict
    return render(request, "reportlist.html", {'form': newdict, 'dates' : missdates})
    