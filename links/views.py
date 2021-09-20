from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from .serializers import LinkSerializer
from .serializers import LinkUpdateSerializer
from .models import Link

class ListLinkAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    
class CreateLinkAPIView(CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    
class UpdateLinkAPIView(UpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkUpdateSerializer

class DeleteLinkAPIView(DestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    
class VisitLinkAPIView(UpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    lookup_field = 'title'
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.visits += 1
        instance.save()
        
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid()
        self.perform_update(serializer)
        
        return Response(serializer.data)
