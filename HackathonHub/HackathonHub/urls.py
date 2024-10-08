"""
URL configuration for HackathonHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from authentication import views as auth_view
from api    import views as api_view
from core   import views as core_view
from real_time_collaboration import views as real_view
from real_time_collaboration.sockets import routing




urlpatterns = [
    path("admin/", admin.site.urls),
    path('login', auth_view.Signin, name='signin'),
    path('logout/',auth_view.signout),
    path("signup",auth_view.signup),
    path("",core_view.subjects_and_schedules),
    path("api/",api_view.hello),
    path("api/subject/",api_view.subject),
    path('rooms', real_view.rooms, name='rooms'),
    path('room/<int:pk>/', real_view.room, name='room'),
    path('code-editor/', real_view.code_editor_view),
    path("assigment", core_view.assigments),
    path('chat/', core_view.chat, name='chat'),
    path("hello/",core_view.data),
    path("calendar",core_view.calendra)
    
   # path('create/', core_view.create_class, name='create_class'),
    #path('list/', core_view.class_list, name='class_list'),

]
