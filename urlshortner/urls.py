"""urlshortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shortner.urls'))
]

# Example of a "null pointer exception" in Python
 
# Initialize variable as None
my_variable = None
 
# Try to access an attribute or method of None (this will raise an AttributeError)
try:
    my_variable.some_method()  # This will fail because None has no attribute 'some_method'
except AttributeError as e:
    print(f"Error: {e}")
