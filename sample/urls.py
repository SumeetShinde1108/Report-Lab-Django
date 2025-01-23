from django.urls import path
from django.contrib import admin
from sample_app.views  import generate_pdf_view


urlpatterns = [
    path("generate_pdf/",generate_pdf_view),
    path("admin/", admin.site.urls),
]
