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

    AvgPriceListApiView,
    ProductFilterApiView,
    FilterPriceApiView,
    MinPriceApiView,
    MaxPriceApiView,
    Revenue,
    Dashboard,
)

urlpatterns = [
    path('filter_prod/', ProductFilterApiView.as_view(), name='filter_prod'),
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

    path('avg/', AvgPriceListApiView.as_view(), name='avg'),
    path('filter_price/<int:price>/', FilterPriceApiView.as_view(), name='filter-price'),
    path('min/',  MinPriceApiView.as_view(), name='min'),
    path('max/',  MaxPriceApiView.as_view(), name='max'),
    path('revenue/',  Revenue.as_view(), name='revenue'),
    path('dashboard/',  Dashboard.as_view(), name='dashboard'),
]

