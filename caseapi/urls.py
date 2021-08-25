from rest_framework import routers
from . import views 

router = routers.DefaultRouter()
router.register(r'cases', views.CaseMetaViewSet)
router.register(r'judges', views.JudgeViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'us/appellate/cases', views.USCircuitCaseMetaViewSet)
router.register(r'us/judges', views.USJudgeViewSet)

urlpatterns = router.urls