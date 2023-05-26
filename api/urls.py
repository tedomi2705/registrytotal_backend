from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'inspection', views.InspectionViewSet)
router.register(r'inspectioncenter', views.InspectionCenterViewSet)
router.register(r'inspectionrecord', views.InspectionRecordViewSet)
router.register(r'owner', views.OwnerViewSet)
router.register(r'upload', views.UploadViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'vehicle', views.VehicleViewSet)
router.register(r'inspectionrecordbycenter', views.InspectionRecordByCenterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
