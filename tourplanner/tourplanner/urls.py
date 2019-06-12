
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('planner/', include('planner.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
