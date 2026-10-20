from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.contrib.auth import authenticate,get_user_model, login as auth_login, logout

User = get_user_model()

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        password = request.POST['password']
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            auth_login(request, user)
            return redirect('Blog_list')
        else:
            return render(request,'login.html',{'error':'Invalid Credentials'})
    return render(request, 'login.html')
@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('Blog_list')

@login_required
def Blog_list(request):
    blog = Blog.objects.select_related(
        'user'
    ). order_by('-id')
    return render(
        request,'Blog_list.html',{'blog':blog}
    )
@login_required
def create_blog(request):
    if request.method == 'POST':
        
        title = request.POST['title']
        description = request.POST['description']

        Blog.objects.create(
            user=request.user,
            title = title,
            description=description
        )
        return redirect('Blog_list')
    return render(request,'create_blog.html')

@login_required
def edit_blog(request,blog_id):
    blog= get_object_or_404(
        Blog, id = blog_id, user = request.user
    )
    if request.method == 'POST':
        
        blog.title = request.POST['title']
        blog.description=request.POST['description']
        blog.save()

        return redirect('Blog_list')
    return render(request,'edit_blog.html',{'blog':blog})

@login_required
def delete_blog(request,blog_id):
    blog = get_object_or_404(
        Blog,id=blog_id,user=request.user
    )
    if request.method == 'POST':
        blog.delete()
        return redirect('Blog_list')

    return render(request,'delete_blog.html',{'blog':blog})

