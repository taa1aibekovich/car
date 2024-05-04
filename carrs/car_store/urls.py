from .views import CategoryView,ProductDetailView
from django.urls import path, include


urlpatterns = [
    path('', CategoryView.as_view(), name='category_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='category_datail')

]
