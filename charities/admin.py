from django.contrib import admin

# Register your models here.
from .models import Charity, Company, User, Upvote

class CharityAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','image_url', 'description']
	class Meta: 
		model = Charity

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','charity','upvote_val']
	class Meta: 
		model = Company

class UserAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	class Meta: 
		model = User

class UpvoteAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','upvotes']
	class Meta:
		model = Upvote

admin.site.register(Charity, CharityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Upvote, UpvoteAdmin)