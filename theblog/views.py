from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Region, Cultivation
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

#def home(request):
    #return render(request, 'home.html', {})
    
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        reg_menu = Region.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["reg_menu"] = reg_menu
        return context

    
    #def get_context_data(self, *args, **kwargs):
        #reg_menu = Region.objects.all()
        #context = super(HomeView, self).get_context_data(*args, **kwargs)
        #context["reg_menu"] = reg_menu
        #return context

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats)
	return render(request, 'categories.html', {'cats':cats.replace('-', ' ').title(), 'category_posts':category_posts})
    
def RegionView(request, regs):
	region_posts = Post.objects.filter(region=regs.replace('-', ' '))
	return render(request, 'regions.html', {'regs':regs.replace('-', ' ').title(), 'region_posts':region_posts})

def CultivationView(request, cults):
	cultivation_posts = Post.objects.filter(cultivation=cults)
	return render(request, 'cultivations.html', {'cults':cults.replace('-', ' ').title(), 'cultivation_posts':cultivation_posts})
    
class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'
    
class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields = ('title', 'body')
    
class AddCategoryView(CreateView):
	model = Category
	#form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'
	#fields = ('title', 'body')
    
class AddRegionView(CreateView):
	model = Region
	#form_class = PostForm
	template_name = 'add_region.html'
	fields = '__all__'
	#fields = ('title', 'body')

class AddCultivationView(CreateView):
	model = Cultivation
	#form_class = PostForm
	template_name = 'add_cultivation.html'
	fields = '__all__'
	#fields = ('title', 'body')
   
class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	#fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')