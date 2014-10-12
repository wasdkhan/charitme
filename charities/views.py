from django.shortcuts import render, HttpResponseRedirect, Http404

from .forms import CompanyForm
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
