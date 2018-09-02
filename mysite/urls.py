from django.conf.urls import include, url
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views
#from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),    
    #url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls')),
    path('polls/', include('polls.urls')),
    #path('admin/', admin.site.urls),
]
