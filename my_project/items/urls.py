# items/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from items.views.item_view import ItemViewSet
from items.views.auth_views import RegisterView, LoginView
from items.opencv_utils.view import ImageProcessingView

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('register/', RegisterView.as_view(), name='register'),  # Registration
    path('login/', LoginView.as_view(), name='login'),  # Login
    path('', include(router.urls)),
    path('convert-image/', ImageProcessingView.as_view(), name='convert-image'),
]
