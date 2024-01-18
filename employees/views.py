from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Post,Staff, Message
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, 'employees/base.htm')

@method_decorator(login_required(login_url='employees:login-page'), name='get') 
class BlogPageView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts':posts
        }
        return render(request, 'employees/blog.htm', context)
    
class ServicePageView(View):
    def get(self, request):
        return render(request, 'employees/services.htm')

@method_decorator(login_required(login_url='employees:login-page'), name='get')    
class PricePageView(View):
    def get(self, request):
        return render(request, 'employees/price.htm')

@method_decorator(login_required(login_url='employees:login-page'), name='get')     
class QuotePageView(View):
    def get(self, request):
        return render(request, 'employees/quote.htm')

@method_decorator(login_required(login_url='employees:login-page'), name='get')     
class TeamPageView(View):
    def get(self, request):
        staff = Staff.objects.all()
        context = {
            'staff':staff
        }
        return render(request, 'employees/team.htm', context)

@method_decorator(login_required(login_url='employees:login-page'), name='get')     
class TestimonialPageView(View):
    def get(self, request):
        return render(request, 'employees/testimonial.htm')

@method_decorator(login_required(login_url='employees:login-page'), name='get')     
class ContactPageView(View):
    def get(self, request):
        return render(request, 'employees/contact.htm')
    def post(self, request):
        name = request.POST['username']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        newcontact = Message.objects.create(name=name, email=email, subject=subject, message=message)
        newcontact.save()
        messages.success(request, "We have received your message. Thankyou for contacting Uncle P Edits. We'll get back to you soon")
        return redirect('employees:home-page')

@method_decorator(login_required(login_url='employees:login-page'), name='get')     
class FeaturePageView(View):
    def get(self, request):
        return render(request, 'employees/feature.htm')

class AboutPageView(View):
    def get(self, request):
        return render(request, 'employees/about.htm')

@method_decorator(login_required(login_url='employees:login-page'), name='get')     
class PostDetailView(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        context = {
            'post':post,
        }
        return render(request, 'employees/post-details.htm', context)
    
class LoginView(View):
    def get(self, request):
        return render(request, 'employees/authentication/login.htm')
    
    def post(self, request):
           
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('employees:home-page')
        else:
            messages.info(request, "Credentials do not match")
            return redirect('employees:login-page')
        
        return render(request, 'employees/authentication/login.htm')

class RegisterView(View):
    def get(self, request):
        return render(request, 'employees/authentication/register.htm')
    
    def post(self, request):
        users = User.objects.all()
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.warning(request, "Passwords do not match")
            return redirect('employees:register-page')
        if len(password1) and len(password2) < 8:
            messages.warning(request, "Password must be 8 or more characters")
            return redirect('employees:register-page')

        exists = User.objects.filter(email=email)
        if exists:
            messages.warning(request, "Email already taken")
            return redirect('employees:register-page')
        else:
            user = User.objects.create(username=username, email=email, password=password1)
            user.save()
            messages.success(request, "User created successfully")
            return redirect('employees:login-page')
        return render(request, 'employees/authentication/login.htm')

    
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "successfully logged out")
        return redirect('employees:login-page')
    
class LockScreenView(View):
    def get(self, request):
        return render(request, 'employees/authentication/lockscreen.htm')
    def post(self, request):
        password = request.POST['password1']
        username = request.user.username
        exists = User.objects.filter(username=username)
        if password == exists.password:
            return redirect('employees:home-page')
        else:
            messages.warning(request, "Wrong password")
            return redirect('employees:lockscreen-page')
        

class ContactFormView(View):
    def get(self, request):
        id = request.user.id
        user_instance = get_object_or_404(User, id=id)
        return render(request, 'employees/contact.htm')
    
    def post(self, request):
        name = request.POST['username']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        newcontact = Message.objects.create(name=name, email=email, subject=subject, message=message)
        newcontact.save()
        messages.success(request, "We have received your message. Thankyou for contacting Uncle P Edits. We'll get back to you soon")
        return redirect('employees:home-page')
 
@method_decorator(login_required(login_url='employees:login-page'), name='dispatch')
class CreatePostView(View):
    def get(self, request):
        return render(request, 'employees/create-post.htm')
    
    def post(self, request):
        logged = request.user.username
        author = User.objects.get(username=logged)
        title = request.POST['title']
        posttype = request.POST['posttype']
        description = request.POST['description']
        image = request.FILES['image']
        content = request.POST['content']
        
        blogpost = Post.objects.create(author=author, title=title, posttype=posttype, description=description, content=content)
        blogpost.image = image  
        blogpost.save()
        
        messages.success(request, "You have successfully created a new post")
        return redirect('employees:blog-page')

@method_decorator(login_required(login_url='employees:login-page'), name='post')
class UpdatePostView(View):
    def get(self, request, pk):

        post = get_object_or_404(Post, id=pk)


        if request.user != post.author:
            messages.error(request, "You don't have permission to edit this post.")
            return redirect('employees:blog-page')

        context = {
            'post': post,
        }
        return render(request, 'employees/update-post.htm', context)
    
    def post(self, request, pk):

        post = get_object_or_404(Post, id=pk)


        if request.user != post.author:
            messages.error(request, "You don't have permission to edit this post.")
            return redirect('employees:blog-page')


        post.title = request.POST['title']
        post.posttype = request.POST['posttype']
        post.description = request.POST['description']
        post.content = request.POST['content']

        if 'image' in request.FILES:
            post.image = request.FILES['image']

        post.save()

        messages.success(request, "Post updated successfully")
        return redirect('employees:blog-page')
    
@method_decorator(login_required(login_url='employees:login-page'), name='dispatch')
class DeletePostView(View):
    def get(self, request, pk):
        return render(request, 'employees/delete-post.htm')
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        if request.user != post.author:
            messages.warning(request, "You don't have permissions to edit this post.")
            return redirect('employees:blog-page')
        post.delete()
        messages.success(request, "Post deleted successfully")
        return redirect('employees:blog-page')
    
