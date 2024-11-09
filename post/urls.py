from django.urls import path
from .views import HomePageView, usuarioView, UpdatePageView
from post.views import CreateView, DetailPageView, DeletePageView

urlpatterns = [
    path("", HomePageView.as_view(), name = "post"),
    path("usuario",usuarioView.as_view(), name= "usuario"),
    path("post/create",CreateView.as_view(),name="create"),
    path("post/detail/<int:pk>", DetailPageView.as_view(), name="detail"),
    #aquii
    path("post/detail/<int:pk>/update",UpdatePageView.as_view(),name="update"),
    path("post/detail/<int:pk>", DetailPageView.as_view(), name="detail"),
     path("post/detail/<int:pk>", DeletePageView.as_view(), name="delete"),

]