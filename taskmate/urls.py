from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views
from users_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact', todolist_views.contact, name='contact'),
    path('about-us', todolist_views.about, name='about'),
    path('todolist/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('', todolist_views.index, name='index')
]
