from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^create/', views.CreateLinkAPIView.as_view(), name='create_link'),
    url(r'^update/(?P<pk>\d+)/', views.UpdateLinkAPIView.as_view(), name='update_link'),
    url(r'^delete/(?P<pk>\d+)/', views.DeleteLinkAPIView.as_view(), name='delete_link'),
    url(r'^visit/(?P<title>[0-9A-Za-z_\-]+)/', views.VisitLinkAPIView.as_view(), name='visit_link'),
    url(r'^list/', views.ListLinkAPIView.as_view(), name='list_link'),
]
