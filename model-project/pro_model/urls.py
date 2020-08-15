from rest_framework import routers
from pro_model import views

router = routers.DefaultRouter()

router.register('test', views.TestViewSet)

urlpatterns = router.urls