from django.urls import path
from .views import * 

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('category/<str:id>/', CategoryListView.as_view(), name='home_detail'),    
    path('mark/<str:id>/', MarkListView.as_view(), name='home_detail_detail'),    
    path('product/<str:id>/', ProductListView.as_view(), name='product'),   
    path('about/<int:id>/', AboutDetailView.as_view(), name='about'),    


]