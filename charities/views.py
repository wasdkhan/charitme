from django.shortcuts import render, HttpResponse, HttpResponseRedirect, Http404

from .forms import CompanyForm, CharityForm, UserForm
from .models import Company, Charity, User

def company(request):
	form = CompanyForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		# name = form.cleaned_data['name']
		# new_join, created = Company.objects.get_or_create(name=name)
		new_join.save()

	template = 'company.html'
	charity_list = Charity.objects.all()
	# return HttpResponse(output)
	context = {'charity_list': charity_list, 'form': form}
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

def index(request):
    charity_list = Charity.objects.order_by('-upvotes')
    # output = ', '.join([p.name for p in charity_list])
    # return HttpResponse(output)
    context = {'charity_list': charity_list}
    return render(request, 'index.html', context)
