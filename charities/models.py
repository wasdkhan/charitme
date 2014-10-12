from django.db import models

class Charity(models.Model):
	name = models.CharField(max_length=200)
	youtube_url = models.URLField(max_length=200)
	upvotes = models.IntegerField()
	description = models.CharField(max_length=500)

	def __unicode__(self):
		return self.name

class Company(models.Model):
	name = models.CharField(max_length=200)
	charity_id = models.IntegerField()
	upvote_val = models.FloatField()
	start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	end_time = models.DateTimeField(auto_now=False, auto_now_add=False)

	def __unicode__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name
