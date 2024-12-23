from core.apps.history.models import BrandHistory


class HistoryService:
    def get_history_items(self):
        objects = BrandHistory.objects.all()
        return objects


history_service = HistoryService()
