from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin

# URLs padrão sem internacionalização
urlpatterns = [
    # Outras rotas que não precisam de tradução ou idioma na URL podem ficar aqui.
]

# URLs com suporte a múltiplos idiomas
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('website.urls')),  # Inclui as rotas do app 'website'
    prefix_default_language=False,  # Define se o idioma padrão deve ser exibido na URL
)

