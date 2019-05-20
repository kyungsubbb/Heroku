from django.contrib import admin
from django.urls import path, include
import blog.views
import word.views
import accounts.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('accounts/',include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('word/', include('word.urls')),

]