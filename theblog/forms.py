from django import forms
from .models import Post, Category, Region, Cultivation, Alertlevel


#choices = [('ΤΙΜΗ ΒΑΜΒΑΚΙΟΥ', 'ΤΙΜΗ ΒΑΜΒΑΚΙΟΥ'), ('ΑΜΠΕΛΙ', 'ΑΜΠΕΛΙ'), ('ΚΑΙΡΟΣ', 'ΚΑΙΡΟΣ'),]
choices =  Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
	choice_list.append(item)


#choices = [('Thessaly', 'Thessaly'), ('Macedonia', 'Macedonia'), ('Creta', 'Creta'),]
choices =  Region.objects.all().values_list('name','name')

choice_list1 = []

for item in choices:
	choice_list1.append(item)
    
#choices = [('Thessaly', 'Thessaly'), ('Macedonia', 'Macedonia'), ('Creta', 'Creta'),]
choices =  Cultivation.objects.all().values_list('name','name')

choice_list2 = []

for item in choices:
	choice_list2.append(item)
    
#choices = [('Thessaly', 'Thessaly'), ('Macedonia', 'Macedonia'), ('Creta', 'Creta'),]
choices =  Alertlevel.objects.all().values_list('name','name')

choice_list3 = []

for item in choices:
	choice_list3.append(item)

class PostForm(forms.ModelForm):
    class Meta:
            model = Post
            fields = ('title', 'title_tag', 'author', 'category', 'region', 'cultivation','alertlevel', 'body','snippet')     
            widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                #'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
                'author': forms.Select(attrs={'class': 'form-control'}),
                'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
                'region': forms.Select(choices=choice_list1, attrs={'class': 'form-control'}),
                'cultivation': forms.Select(choices=choice_list2 , attrs={'class': 'form-control'}),
                'alertlevel': forms.Select(choices=choice_list3  , attrs={'class': 'form-control'}),
                'body': forms.Textarea(attrs={'class': 'form-control'}),			
                'snippet': forms.Textarea(attrs={'class': 'form-control'}),			
            }
            
class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'body', 'snippet')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),			
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),			
		}