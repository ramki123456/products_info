from __future__ import unicode_literals

from django.db import models

# Create your models here.

class StockDetails(models.Model):
	product_name = models.CharField(max_length=40)
	product_bar_no = models.CharField(max_length=20)
	price = models.FloatField()
	quantity = models.IntegerField()

	def __unicode__(self):
		return self.product_name

class Employe(models.Model):
	emp_id=models.IntegerField()
	company_name=models.CharField(max_length=50)
	stockdetails_data=models.ForeignKey(StockDetails)
	def __unicode__(self):
		return self.company_name
