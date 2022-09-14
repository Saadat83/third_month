from django.urls import path
from .views import(
    ProductListApiView,
    ProductCreateApiView,
    ProductDetailApiView,
    ProductUpdateApiView,
    ProductDestroyApiView,
    CategoryListApiView,
    CategoryCreateApiView,
    CategoryDetailApiView,
    CategoryDestroyApiView,
    CategoryUpdateApiView,
)

urlpatterns = [
    path('prod_list/', ProductListApiView.as_view(), name='prod-list'),
    path('prod_create/', ProductCreateApiView.as_view(), name='prod-create'),
    path('detail/<int:id>/', ProductDetailApiView.as_view(), name='detail'),
    path('prod_update/<int:id>/', ProductUpdateApiView.as_view(), name='prod_update'),
    path('prod_delete/<int:id>/', ProductDestroyApiView.as_view(), name='prod_delete'),
    path('cat_list/', CategoryListApiView.as_view(), name='cat_list'),
    path('cat_create/', CategoryCreateApiView.as_view(), name='cat_create'),
    path('cat_update/<int:id>/', CategoryUpdateApiView.as_view(), name='cat_update'),
    path('filter_by_category/<slug:name>/', CategoryDetailApiView.as_view(), name='cat_detail'),
    path('cat_delete/<int:id>/', CategoryDestroyApiView.as_view(), name='cat_delete'),
]

