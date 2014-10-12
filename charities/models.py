from django.db import models

class Charity(models.Model):
	name = models.CharField(max_length=200)
	image_url = models.URLField(max_length=200)
	description = models.CharField(max_length=500)

	def __unicode__(self):
		return self.name

class Upvote(models.Model):
	charity = models.ForeignKey(Charity)
	upvotes = models.IntegerField()

	def __unicode__(self):
		return self.charity.name

class Vote(models.Model):
	voter = models.ForeignKey('User')
	link = models.ForeignKey(Charity)

	def __unicode__(self):
		return "%s voted %s" % (self.voter.name, self.link.name)

class Company(models.Model):
	name = models.CharField("Company Title", max_length=200)
	charity = models.ForeignKey(Charity)
	upvote_val = models.FloatField("Value per upvote")
	start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	end_time = models.DateTimeField(auto_now=False, auto_now_add=False)

	def __unicode__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name