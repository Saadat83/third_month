Documetnation:
Для написания этой программы я использовала следующие библиотеки:

asgiref==3.5.2
Django==4.1.1
django-filter==22.1
djangorestframework==3.13.1
djangorestframework-simplejwt==5.2.0
peewee==3.15.1
Pillow==9.2.0
psycopg2==2.9.3
PyJWT==2.4.0
pytz==2022.2.1
sqlparse==0.4.2
tzdata==2022.2
Эти библиотеки вы можете скачать по команде: pip install -r req.txt


У меня есть 2 app(account, product), также главная app (saadat_project)
В settings для того чтобы программа видела наши папки мы вводим названия в INSTALLED_APPS :

INSTALLED_APPS = [
    ...
    'account',
    'rest_framework',
    'product',
    'django_filters',
]

В папке 'saadat_project.url'  я прописала главные пути, которые используются при работе с браузером:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls')),
    path('api/product/', include('product.urls')),
]

Папка product.view содержит всю логику для работы с продуктами, а также бухгалтерский учет
Пути которые присутствуют в urls.py
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
    path('filter_price/<int:price>/', PriceApiView.as_view(), name='filter-price'),
    path('min/',  MinPriceApiView.as_view(), name='min'),
    path('max/',  MaxPriceApiView.as_view(), name='max'),
    path('revenue/',  Revenue.as_view(), name='revenue'),

]


Папка account.view содержит всю логику для работы с user
Пути которые присутствуют в urls.py:
urlpatterns = [
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('list/', UserListApiView.as_view(), name='user'),
    path('user_detail/<int:id>', UserDetailApiView.as_view(), name='user_detail'),
    path('delete/<int:id>/', UserDestroyApiView.as_view(), name='delete'),
]


Для того чтобы все заработало необходимо в терминале ввести:
1. 'python manage.py makemigrations'- отвечает за упаковку изменений вашей модели в отдельные файлы миграции — аналогично коммитам
2. 'python manage.py migrate' — migrate отвечает за их применение к вашей базе данных
3. 'python manage.py runserver' - для запуска программы

