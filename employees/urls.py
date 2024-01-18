from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('blog/', views.BlogPageView.as_view(), name='blog-page'),
    path('about/', views.AboutPageView.as_view(), name='about-page'),
    path('services/', views.ServicePageView.as_view(), name='service-page'),
    path('feature/', views.FeaturePageView.as_view(), name='feature-page'),
    path('pricing/', views.PricePageView.as_view(), name='price-page'),
    path('quote/', views.QuotePageView.as_view(), name='quote-page'),
    path('team/', views.TeamPageView.as_view(), name='team-page'),
    path('testimonial/', views.TestimonialPageView.as_view(), name='testimonial-page'),
    path('contact/', views.ContactPageView.as_view(), name='contact-page'),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('auth/login/', views.LoginView.as_view(), name='login-page'),
    path('auth/register/', views.RegisterView.as_view(), name='register-page'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout-page'),
    path('auth/lockscreen/', views.LockScreenView.as_view(), name='lockscreen-page'),
    path('info/', views.ContactFormView.as_view(), name='contactform-page'),
    path('createblog/', views.CreatePostView.as_view(), name='post-page'),
    path('delete-post/<int:pk>/', views.DeletePostView.as_view(), name='post-delete'),
    path('update-post/<int:pk>/', views.UpdatePostView.as_view(), name='post-update'),

]