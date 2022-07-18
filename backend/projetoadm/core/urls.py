from codecs import namereplace_errors
from django.urls import path
from projetoadm.core import views as v

app_name='core'

urlpatterns=[
    path('api/policial/', v.api_policial,name='policial'),
    # path('api/policial/', v.PolicialListView.as_view())
]