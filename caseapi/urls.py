from rest_framework import routers
from . import views 

router = routers.DefaultRouter()
router.register(r'cases', views.CaseMetaViewSet)
router.register(r'us/cases', views.USCaseMetaViewSet)

urlpatterns = router.urls