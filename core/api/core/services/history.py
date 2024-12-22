from core.apps.history.models import BrandHistory


class HistoryService:
    def get_history_items(self):
        return BrandHistory.objects.all()


history_service = HistoryService()
