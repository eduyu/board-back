from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/articles/', include('articles.urls')),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/signup/', include('rest_auth.registration.urls')),
]
