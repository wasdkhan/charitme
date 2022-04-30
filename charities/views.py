from django.shortcuts import render, HttpResponse, HttpResponseRedirect, Http404, get_object_or_404

from .forms import CompanyForm, CharityForm, UserForm, UpvoteForm
from .models import Company, Charity, User, Upvote

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
		u = Upvote(charity=new_join,upvotes=0)
		u.save()

	context = {'form': form}
	template = 'charity.html'
	return render(request, template, context)

def charityp(request, charity_id):
	upvote = get_object_or_404(Upvote, pk=charity_id)
	if 'choice' in request.POST:
		upvote.upvotes += 1
		upvote.save()

	# try:
	# 	selected_choice = p.choice_set.get(pk=request.POST['choice'])
	# except (KeyError, Upvote.DoesNotExist):
 #        # Redisplay the poll voting form.
 #        return render(request, 'index.html', {    
 #        	'poll': p,
 #        	'error_message': "You didn't select a choice.",
 #        })
 #    else:
 #        selected_choice.upvotes += 1
 #        selected_choice.save()
 #        # Always return an HttpResponseRedirect after successfully dealing
 #        # with POST data. This prevents data from being posted twice if a
 #        # user hits the Back button.
 #        return HttpResponseRedirect(reverse('charities:index')

	return render(request, 'charityp.html', {'upvote': upvote})
	
	# return HttpResponse("You're looking at charity %s." % charity_id)

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
    # charity_list = Charity.objects.order_by('-upvotes')        
    upvotes_list = Upvote.objects.order_by('-upvotes') 
    # for upvote in upvotes_list:
    	# upvote.

    # output = ', '.join([p.name for p in charity_list])
    # return HttpResponse(output)
    context = {'upvotes_list': upvotes_list,}
    return render(request, 'index.html', context)
