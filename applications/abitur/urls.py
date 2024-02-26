from django.urls import path

from .views import ApplicantAPIView, ApplicantDetailAPIView

urlpatterns = [
    path('detail/<int:appl_id>/', ApplicantDetailAPIView.as_view(), name='applicant-detail'),
    path('list/', ApplicantAPIView.as_view(), name='applicant-list'),
]