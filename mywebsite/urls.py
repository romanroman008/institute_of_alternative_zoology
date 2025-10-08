"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

def dbcheck(_request):
    try:
        with connection.cursor() as cur:
            cur.execute("SELECT version(), current_database(), current_user")
            version, dbname, dbuser = cur.fetchone()
            # czasem użyteczne: adres serwera
            try:
                cur.execute("SELECT inet_server_addr()::text, inet_server_port()")
                host, port = cur.fetchone()
            except Exception:
                host, port = "(n/a)", "(n/a)"
        payload = {
            "engine": connection.settings_dict.get("ENGINE"),
            "name": connection.settings_dict.get("NAME"),
            "user": dbuser,
            "host": connection.settings_dict.get("HOST"),
            "port": connection.settings_dict.get("PORT"),
            "server_addr": host,
            "server_port": port,
            "version": version,
        }
        return HttpResponse(json.dumps(payload, indent=2), content_type="application/json", status=200)
    except Exception as e:
        return HttpResponse(f"DB ERROR: {e}", status=500)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url=reverse_lazy("myapp:index"), permanent=False)),
    path('myapp/', include('myapp.urls')),
    path('users/', include('users.urls')),
    path("dbcheck/", dbcheck),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
