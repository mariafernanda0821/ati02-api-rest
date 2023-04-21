from django.contrib import admin
from django.urls import path
from .views import users, postDeUnUsuario


app_name = "admin_user"
#path('my-view/<int:id>/', views.my_view, name='my-view'),
urlpatterns = [
    path('', users, name='users'),
    path('post-user/<int:id>/', postDeUnUsuario, name="post_user")
]