from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .models import PostModel

# Create your views here.

class PostDetailView(DetailView):
    model = PostModel
    template_name = 'main/detail.html'



class CreateView(CreateView):
    model = PostModel
    template_name = 'main/create.html'
    fields = ['name', 'body', 'image']
    success_url = '/'
    
    
    
class HomeView(ListView):
    queryset = PostModel.objects.all()
    template_name = 'main/home.html'
    
    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search:
            qs = PostModel.objects.filter(name__icontains=search)
        else:
            qs = PostModel.objects.all()
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[ 'title' ] = 'Home page'
        context[ 'q' ] = self.request.GET.get('search', '')
        return context
        
        
        
# def home_view(request,):
#     posts = PostModel.objects.all()
#     return render(request, 'main/home.html', context={
#         'posts': posts,
#         'title': 'hello'
#     }