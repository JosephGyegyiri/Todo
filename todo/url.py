from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TodoListViewSet



router = DefaultRouter()
router.register('', TodoListViewSet, basename='todo-list')



urlpatterns = router.urls