
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView


# API
api_patterns = [
    url(r'^', include('api.urls')),
]

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(api_patterns)),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', RedirectView.as_view(pattern_name='admin:login', permanent=False)),
    # url(r'^nested_admin/', include('nested_admin.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
