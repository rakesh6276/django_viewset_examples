from .serializers import LanguageSerializer
from .models import language
from rest_framework import viewsets, permissions

class languageView(viewsets.ModelViewSet):
    queryset = language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

