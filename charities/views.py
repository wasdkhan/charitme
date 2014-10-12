from django.shortcuts import render, HttpResponseRedirect, Http404

from .forms import CompanyForm, CharityForm, UserForm	
from .models import Company

def company(request):
	form = CompanyForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		# name = form.cleaned_data['name']
		# new_join, created = Company.objects.get_or_create(name=name)
		new_join.save()

	context = {'form': form}
	template = 'company.html'
	return render(request, template, context)

def charity(request):
	form = CharityForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		# name = form.cleaned_data['name']
		# new_join, created = Company.objects.get_or_create(name=name)
		new_join.save()

	context = {'form': form}
	template = 'charity.html'
	return render(request, template, context)

def user(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		# name = form.cleaned_data['name']
		# new_join, created = Company.objects.get_or_create(name=name)
		new_join.save()

	context = {'form': form}
	template = 'user.html'
	return render(request, template, context)