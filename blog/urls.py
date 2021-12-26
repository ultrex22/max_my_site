from django.conf.urls.static import static
from django.urls import path

from max_my_site import settings
from . import views

urlpatterns = [
                  # path('', views.starting_page, name='starting-page'),
                  path('', views.StartingPageView.as_view(), name='starting-page'),
                  path('posts', views.PostsView.as_view(), name='posts-page'),
                  path('posts/<slug:slug>', views.SinglePostDetail.as_view(), name='post-detail-page'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
