from . import views
from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'inspection', views.InspectionViewSet)
router.register(r'inspectioncenter', views.InspectionCenterViewSet)
router.register(r'inspectionrecord', views.InspectionRecordViewSet)
router.register(r'owner', views.OwnerViewSet)
router.register(r'upload', views.UploadViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'vehicle', views.VehicleViewSet)
router.register(r'inspectionrecordbycenter', views.InspectionRecordByCenterViewSet)
router.register(r'register', views.UserRegisterView)
router.register(r'user/me',views.LoggedInUserViewSet,basename='me')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
