from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
#     path('account/', include('account.urls')),
]+ i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('cart/', include('cart.urls')),
    path('contact/', include('contact.urls')),
)

