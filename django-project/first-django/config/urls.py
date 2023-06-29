from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('<str:id>', blog.views.detail, name="detail"),
    path('new/', blog.views.new, name="new"),
    path('create/', blog.views.create, name="create"),
    path('edit/<str:id>', blog.views.edit, name="edit"),
    path('update/<str:id>', blog.views.update, name="update"),
    path('delete/<str:id>', blog.views.delete, name="delete"),
    path('map/', blog.views.viewMap),
    path('like_post/<int:blog_id>/', blog.views.like_post, name='like_post'),
    path('add_comment/<int:blog_id>/', blog.views.add_comment, name='add_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
