from django.urls import path

from . import views

urlpatterns = [
    path('', views.researchers, name="researchers"),
    path('<int:researcher_id>/', views.researcher, name="researcher"),
    # path('blogs/', include('blogs.urls')),
] 



urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('<int:blog_id>/', views.blog, name="blog"),
    # path('blogs/', include('blogs.urls')),
] 
