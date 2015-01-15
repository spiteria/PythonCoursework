from django.conf.urls import patterns, include, url
from django.contrib import admin
from Monte import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoMonteCarlo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^monte$', views.mainview, name='index'),
    url('^pi$', views.findPi, name='findPi'),
    #url(r'^admin/', include(admin.site.urls)),
)
