from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route

urlpatterns = [
    # Root route - should be at the very top
    path('', root_route),

    # Admin route
    path('admin/', admin.site.urls),

    # Authentication routes
    path('api-auth/', include('rest_framework.urls')),
    
    # Logout route - needs to be before dj-rest-auth
    path('dj-rest-auth/logout/', logout_route),
    
    # Dj-rest-auth routes
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    
    # Dj-rest-auth registration routes
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # Application-specific routes with explicit prefixes to avoid clashes
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
    path('comments/', include('comments.urls')),
    path('likes/', include('likes.urls')),
    path('followers/', include('followers.urls')),
]
