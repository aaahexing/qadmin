from django.http import HttpResponse
from rest_framework import viewsets

from .models import Question
from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the questions index.")