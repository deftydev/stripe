from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import (
    login,
    logout,
    signup,
)

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login,name='login'),
    path('logout/', logout,name='logout'),
    path('signup/', signup,name='signup'),
    path('', include('commerce.urls', namespace='commerce'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
