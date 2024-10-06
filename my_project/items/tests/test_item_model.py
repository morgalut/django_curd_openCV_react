# tests/test_item_model.py
from django.test import TestCase
from items.models import Item
from django.contrib.auth.models import User

class ItemModelTestCase(TestCase):

    def setUp(self):
        # Set up user and item for model testing
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.item = Item.objects.create(name="Test Item", description="Test description", created_by=self.user)

    def test_item_creation(self):
        # Test item creation
        item = Item.objects.create(name="New Item", description="New Description", created_by=self.user)
        self.assertEqual(item.name, "New Item")
        self.assertEqual(Item.objects.count(), 2)

    def test_item_string_representation(self):
        # Test the string representation of the item
        self.assertEqual(str(self.item), "Test Item")

    def test_item_created_by_user(self):
        # Test that the item is associated with the correct user
        self.assertEqual(self.item.created_by, self.user)

    def test_item_auto_timestamp(self):
        # Test that the `created_at` field is automatically set
        self.assertIsNotNone(self.item.created_at)