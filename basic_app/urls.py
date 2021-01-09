from django.conf.urls import url
from basic_app import views
urlpatterns=[
        url(r'^$',views.BagListView.as_view(),name='list'),
        url(r'^create/$',views.BagCreateView.as_view(),name='create'),
        url(r'^update/(?P<pk>\d+)/$',views.BagUpdateView.as_view(),name='update'),
        url(r'^delete/(?P<pk>\d+)/$',views.BagDeleteView.as_view(),name='delete'),
        url(r'^search-by-date/$',views.SearchByDateView,name='search-by-date'),

]
