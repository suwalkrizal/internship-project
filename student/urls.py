from django.urls import path,include
from .views import *
from rest_framework import routers

router=routers.SimpleRouter()
router.register(r'student',StudentViewset,basename='student')

urlpatterns = router.urls+[
]