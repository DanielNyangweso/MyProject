from . import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path("", views.home, name="home"),
    path("products", views.products, name="products"),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('api/', include(router.urls)),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

