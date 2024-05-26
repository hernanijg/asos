from django.urls import path
from .views import (UserListCreateApi, UserRetrieveUpdateDestroyApi,
                    ProductListCreateApi, ProductRetrieveUpdateDestroyApi,
                    CommentListCreateApi, CommentRetrieveUpdateDestroyApi,
                    ProductSeeListCreateApi, ProductSeeRetrieveUpdateDestroyApi,
                    ProductLikeListCreateApi, ProductLikeRetrieveUpdateDestroyApi,
                    OrderListCreateApi, OrderRetrieveUpdateDestroyApi,
                    CarListCreateApi, CarRetrieveUpdateDestroyApi)

urlpatterns = [
    path('user/', UserListCreateApi.as_view(), name='user-list-create'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyApi.as_view(), name='user-retrieve-update-destroy'),
    path('product/', ProductListCreateApi.as_view(), name='product-list-create'),
    path('product/<int:pk>', ProductRetrieveUpdateDestroyApi.as_view(), name='product-retrieve-update-destroy'),
    path('comment/', CommentListCreateApi.as_view(), name='comment-list-create'),
    path('comment/<int:pk>/', CommentRetrieveUpdateDestroyApi.as_view(), name='comment-retrieve-update-destroy'),
    path('productsee/', ProductSeeListCreateApi.as_view(), name='productsee-list-create'),
    path('productsee/<int:pk>/', ProductSeeRetrieveUpdateDestroyApi.as_view(), name='productsee-retrieve-update-destroy'),
    path('productlike/', ProductLikeListCreateApi.as_view(), name='productlike-list-create'),
    path('productlike/<int:pk>/', ProductLikeRetrieveUpdateDestroyApi.as_view(), name='productlike-retrieve-update-destroy'),
    path('order/', OrderListCreateApi.as_view(), name='order-create-list'),
    path('order/<int:pk>', OrderRetrieveUpdateDestroyApi.as_view(), name='order-retrieve-update-destroy'),
    path('car/', CarListCreateApi.as_view(), name='car-list-create'),
    path('car/<int:pk>', CarRetrieveUpdateDestroyApi.as_view(), name='car-retrieve-update-destroy'),

]
