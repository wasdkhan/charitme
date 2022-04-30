from django import forms
from django.shortcuts import render

from .models import Company, Charity, User, Upvote

class CompanyForm(forms.ModelForm):
	class Meta: 
		model = Company

class CharityForm(forms.ModelForm):
	class Meta: 
		model = Charity

class UserForm(forms.ModelForm):
	class Meta: 
		model = User

class UpvoteForm(forms.ModelForm):
	class Meta: 
		model = Upvote