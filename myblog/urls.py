from django.conf.urls import patterns, include, url
from blogster import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    #Home Page
    url(r'^$', views.index),
    url(r'^blog/$', views.getPosts),
    url(r'^blog/(?P<selected_page>\d+)/?$', views.getPosts),
    #Displaying a specific post
    url(r'^blog/\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', views.getPost),
    #Display posts from specific category
    url(r'^blog/categories/(?P<categorySlug>\w+)/?$', views.getCategory),
    url(r'^blog/categories/(?P<categorySlug>\w+)/(?P<selected_page>\d+)/?$', views.getCategory),
    #comments
    url(r'^comments/', include('django.contrib.comments.urls')),
    #Flatpages
    url(r'', include('django.contrib.flatpages.urls')),
)
