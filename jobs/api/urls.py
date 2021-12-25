from django.urls import path
# from news.api.views import article_list_create_api_view, article_detail_api_view
from jobs.api.views import JobOfferListCreateAPIView, JobOfferDetailAPIView


urlpatterns = [
    path('jobs/', JobOfferListCreateAPIView.as_view(), name='job-list'),
    path('jobs/<int:pk>', JobOfferDetailAPIView.as_view(), name='job-detail'),
]
