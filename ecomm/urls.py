from django.urls import include, path  # check if this is correct
from rest_framework import routers
from user import views
from django.contrib import admin
router = routers.DefaultRouter()
#router.register(r'abc', views.AbcView, basename='abc')
router.register(r'login', views.LoginViewSet, basename='login')
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'cart', views.CartViewSet, basename='cart')
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'seller', views.SellerViewSet, basename='seller')
router.register(r'seller', views.CategoryViewSet, basename='category')





# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
         namespace='rest_framework')),  # not sure about thi
    path('admin/', admin.site.urls)
]

from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]