from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Type(models.Model):
	name = models.CharField(max_length=50, unique=True)
	
	
	
class Menus(models.Model):
	number = models.CharField(max_length=10,default='', unique=True)
	name = models.CharField(max_length=200)
	price = models.DecimalField(decimal_places=2,max_digits=10)
	description = models.CharField(max_length=200, blank=True, default='')
	#image = models.ImageField(null=True)
	type = models.ForeignKey('Type', on_delete = models.SET_NULL, null=True, blank=True)
	active = models.BooleanField(default=True)
	
	def __str__(self):
		return "Name:"+self.name+", price: "+str(self.price) +", description: "+self.description

class Orders(models.Model):
	time = models.DateTimeField()
	user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
	sum_price = models.DecimalField(decimal_places=2,max_digits=10)
	tip = models.DecimalField(decimal_places=2,max_digits=10)
	deliver_fee = models.DecimalField(decimal_places=2,max_digits=10)
	total = models.DecimalField(decimal_places=2,max_digits=10)
	Address = models.CharField(max_length = 100)
	phone = models.CharField(max_length = 10) 
	


class OrderItems(models.Model):
	item = models.ForeignKey('Menus', on_delete = models.SET_NULL, null=True)
	number = models.IntegerField(default=timezone.now)
	order_number = models.ForeignKey('Orders', on_delete = models.CASCADE)

	
	
	
	
