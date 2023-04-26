from codecs import namereplace_errors
from email.mime import base
from xml.etree.ElementInclude import include
from django.urls import path , include


from .views import GraduacaoViewSet, PolicialViewSet, PostoViewSet
from projetoadm.core import views as v
from rest_framework.routers import DefaultRouter

app_name='core'

router= DefaultRouter()
router.register("policiais",PolicialViewSet,basename="policiais"),
router.register("postos",PostoViewSet,basename="postos"),
router.register("graduacoes",GraduacaoViewSet,basename="graduacoes")


urlpatterns=[
    # path('api/policial/', v.policialList,name='policialList'),
    # path('api/policial-detail/<str:pk>/', v.PolicialDetail,name='policialDetail'),
    # path('api/policial-create/', v.policialCreate,name='policialCreate'),
    path('', include(router.urls)),
]