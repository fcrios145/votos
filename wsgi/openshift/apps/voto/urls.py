from django.conf.urls import patterns, include, url

from django.contrib import admin

from .views import Home, Registro, Logout, Votar

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', include('apps.voto.urls')),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'', include('social_auth.urls')),

    url(r'^$', Home.as_view(), name='home'),
    url(r'^registro$', Registro.as_view(), name='registro'),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^salir/', Logout.as_view(), name='logout'),
    url(r'^votar/', Votar.as_view(), name='votar'),


)
