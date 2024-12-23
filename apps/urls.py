from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("post/<int:id>",views.post,name="post"),
    path("make",views.make,name="make"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("logout",views.logout,name="logout"),
    path("signup",views.signup,name="signup")
]