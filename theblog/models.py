from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date, time
#from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')
        
class Region(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')        

class Cultivation(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')

class Alertlevel(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    #header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default='text1')
    #body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    post_time = models.DateTimeField(default = datetime.now, blank = True)
    category = models.CharField(max_length=255, default='coding')
    region = models.CharField(max_length=255, default='thessaly')
    cultivation = models.CharField(max_length=255, default='tomato')
    alertlevel = models.CharField(max_length=255, default='red')
    snippet = models.CharField(max_length=255, default='Snipped')
    
    
    def __str__(self):
            return self.title + ' | ' + str(self.author)
        
    def get_absolute_url(self):
                #return reverse('article-detail', args=(str(self.id)) )
                return reverse('home')