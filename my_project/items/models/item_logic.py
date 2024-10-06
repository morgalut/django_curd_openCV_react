from .item_model import Item
from datetime import timedelta
from django.utils import timezone

class ItemLogic:
    @staticmethod
    def is_recent(item: Item) -> bool:
        """Check if the item was created within the last 7 days."""
        return timezone.now() - item.created_at <= timedelta(days=7)

    @staticmethod
    def item_count_by_user(user) -> int:
        """Return the number of items created by a user."""
        return Item.objects.filter(created_by=user).count()
