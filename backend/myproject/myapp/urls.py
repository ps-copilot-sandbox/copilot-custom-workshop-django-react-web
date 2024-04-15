from django.urls import path
from .views import cat_list, insert_cat

urlpatterns = [
    path('cats/', cat_list),
    path('insert_cat/', insert_cat)
]