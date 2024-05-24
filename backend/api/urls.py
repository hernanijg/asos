from django.urls import path
from .views import TestModelListCreated, TestModelRetrieveUpdateDestroy

urlpatterns = [
    path('testurl/', TestModelListCreated.as_view(), name='test'),
    path('testurl/<int:pk>/', TestModelRetrieveUpdateDestroy.as_view(), name="Cut, put")
]
