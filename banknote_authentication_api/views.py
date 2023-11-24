from rest_framework.views import APIView
from django.db import transaction
from .serializers import *
from django.http import HttpResponse
import json
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from joblib import load

from prediction import *


class ListDataset(ListCreateAPIView):
    queryset = DatasetModels.objects.all()
    serializer_class = DatasetModelsSerializer
    pagination_class = PageNumberPagination


class UploadDataset(APIView):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        model = autoML_fit()
        body = request.body

        try:
            json_data = json.loads(body)
            path = json_data["path"]

        except json.JSONDecodeError as e:
            return HttpResponse(f'Error decoding JSON: {str(e)}', status=400)

        dataset_model_instance, created = DatasetModels.objects.get_or_create(
            file=path,
        )

        dataset_model_instance.serialized_model = model
        dataset_model_instance.save()

        return HttpResponse('POST request processed successfully')


class Predict(APIView):
    @transaction.atomic
    def post(self, request):
        body = request.body

        try:
            json_data = json.loads(body)

        except json.JSONDecodeError as e:
            return HttpResponse(f'Error decoding JSON: {str(e)}', status=400)

        try:
            dataset = DatasetModels.objects.get()

        except DatasetModels.DoesNotExist:
            return JsonResponse({'error': 'Dataset not found'}, status=404)

        X_test = pd.DataFrame([json_data])
        serialized_model = dataset.serialized_model
        cleaned_file_path = serialized_model.strip("[]").replace("'", "")
        model = load(cleaned_file_path)
        file = dataset.file

        X, y = load_dataset(file)

        probability = predict_probability(model, X, y, X_test)

        return JsonResponse({'output ': probability})
