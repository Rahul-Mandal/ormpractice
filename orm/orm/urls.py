"""orm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from myapp.views import *


from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)

router = DefaultRouter()
# router.register(r'api', StudentDetails, basename='user') #ModelViewSet
router.register(r'api', StudentViewset, basename='user')  # ViewSet
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/',home),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
    
    #functioned based
    path('hello/', student_api),
    path('hello/<int:id>', student_api),
    path('hi/', StudentApi1.as_view()),
    path('hi/<int:id>', StudentApi1.as_view()),
    path('plan/', PlanView.as_view()),
    path('plan/<int:pk>', PlanView.as_view()),
    path('update_plan/<int:pk>', UpdatePlan.as_view()),
    
    #class based
    # path('hello/', StudentApi.as_view()),
    # path('hello/<int:pk>', StudentApi.as_view())

    path('sel/', select_re)

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),