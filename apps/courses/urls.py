from django.urls import path

from .views import CourseListView, CourseDetailView, CourseChargeView


urlpatterns = [
  path('', CourseListView.as_view(), name='course_list'),
  path('charge/', CourseChargeView.as_view(), name='charge'),
  path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
]
