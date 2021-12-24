from django.urls import path
from . import views
from max_my_site import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.starting_page, name='starting-page'),
    path('', views.StartingPageView.as_view(), name='starting-page'),
    path('posts', views.PostsView.as_view(), name='posts-page'),
    path('posts/<slug:slug>', views.post_detail, name='post-detail-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
