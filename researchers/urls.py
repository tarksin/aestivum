from django.urls import path

from . import views

urlpatterns = [
    # path('', views.researchers, name="researchers"),
    path('researchers/', views.researchers, name="researchers"),
    path('<int:researcher_id>/', views.researcher, name="researcher")
] 
