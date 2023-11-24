from django.urls import path
from .views import *

urlpatterns = [
    path('datasets/', ListDataset.as_view(), name="ListDatasets"),
    path('datasets/creation', UploadDataset.as_view(), name="UploadDatasets"),
    path('datasets/prediction', Predict.as_view(), name="Predict")
]