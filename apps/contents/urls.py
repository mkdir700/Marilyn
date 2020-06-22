from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('contents', ContentsViewSet, basename='contents')
urlpatterns = router.urls
