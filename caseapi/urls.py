from rest_framework import routers
from . import views 

router = routers.DefaultRouter()
router.register(r'cases', views.CaseMetaViewSet)
router.register(r'us/appellate/cases', views.USCircuitCaseMetaViewSet)

urlpatterns = router.urls