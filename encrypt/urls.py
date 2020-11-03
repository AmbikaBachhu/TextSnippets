"""encrypt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include,re_path
from decrypt import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api',views.Snippetviewset)
from django.contrib.auth import views as auth_views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ShowDetails, name="show"),
    path('save/', views.ShowDetailsSave, name="save"),
    path('show/', include(router.urls)),
    path('users/',views.UserList.as_view()),
    re_path('users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
    # path('get-api-token/',views.obtain_auth_token,name="get-api-token")
    path('auth_jwt/',obtain_jwt_token),
    path('auth_refresh_jwt/',refresh_jwt_token),
    path('auth_verify_jwt/',verify_jwt_token)
]
