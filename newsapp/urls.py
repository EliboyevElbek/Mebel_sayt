from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    contact_view,
    ServicesPageView,
    ListProductView,
    DetailPageView,
    get_category,
    contact_buy,
    search_view,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', contact_view, name='contact'),
    path('buyrutma/<int:pk>/', contact_buy, name='buy'),
    path('category/<str:fstr>/', get_category, name='category'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('detail/<int:pk>/', DetailPageView.as_view(), name='detail_product'),
    path('list-product/', ListProductView.as_view(), name='shop'),
    path('search/', search_view, name='search')
]