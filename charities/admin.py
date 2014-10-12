from django.contrib import admin

# Register your models here.
from .models import Charity, Company

class CharityAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','upvotes', 'description']
	class Meta: 
		model = Charity

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','charity_id','upvote_val']
	class Meta: 
		model = Company

admin.site.register(Charity, CharityAdmin)
admin.site.register(Company, CompanyAdmin)