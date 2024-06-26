from django.conf.urls import url
from . import views


app_name = 'shop'

urlpatterns = [
    url(r'^$', views.get_product_list, name='get_product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.get_product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.get_product_detail,
        name='product_detail'),
]
