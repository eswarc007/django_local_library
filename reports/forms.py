from django.forms import ModelForm
from django import forms
from models import Report




class createReport(ModelForm):
    class Meta:
        model = Report
        fields = ['DateofReport', 'Process', 'Hours']