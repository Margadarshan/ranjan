from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
            ListView,
            CreateView,
            UpdateView,
            DeleteView,
            )
from .models import Post
from django.contrib import messages

# Create your views here.
def post_list(request):
	post_list=Post.objects.all()
	context={'posts':post_list}
	return render(request,'blog/home.html',context)

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','description','img','location']
    # fields=['location','name']
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request,f'You have created a new post!')
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','description','img','location']

    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request,f'You have edited your post!')
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url="/blog"
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        else:
            return False

# def testview(request):
#     form=GeoForm()
#     return render(request,'blog/test.html',{'form':form})