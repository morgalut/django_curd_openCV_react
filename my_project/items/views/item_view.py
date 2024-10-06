from rest_framework import viewsets, status
from rest_framework.response import Response
from items.models.item_model import Item
from items.serializers.item_serializer import ItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Item.DoesNotExist:
            raise NotFound("Item not found.")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
