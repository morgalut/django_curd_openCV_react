from rest_framework import serializers
from items.models.item_model import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description']
    
    def validate_name(self, value):
        """Ensure the name is not empty or too long."""
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        if len(value) > 255:
            raise serializers.ValidationError("Name is too long.")
        return value
