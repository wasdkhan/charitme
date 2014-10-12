from django import forms
from django.shortcuts import render

from .models import Company

class CompanyForm(forms.ModelForm):
	class Meta: 
		model = Company