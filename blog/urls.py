from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from max_my_site import settings
from . import views

admin.site.site_header = 'Blog Admin - Site Header'
admin.site.index_title = "Blog - Index Title"

urlpatterns = [
    # path('', views.starting_page, name='starting-page'),
    path('', views.StartingPageView.as_view(),
         name='starting-page'),
    path('posts', views.PostsView.as_view(), name='posts-page'),
    path('posts/<slug:slug>', views.SinglePostDetail.as_view(),
         name='post-detail-page'),
    path('read-later', views.ReadLaterView.as_view(),
         name='read-later'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
