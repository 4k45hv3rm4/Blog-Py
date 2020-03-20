from django.urls import path
from . import views
app_name="app"
urlpatterns =[
    path("",views.post_list, name="post_list"),
    path("create/",views.post_create, name="post_create"),
    path("update/<int:pk>/",views.post_update, name="post_update"),
    path("delete/<int:pk>/",views.post_delete, name="post_delete"),
    path("detail/<int:pk>/",views.post_detail, name="post_detail"),

]
