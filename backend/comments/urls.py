from django.urls import path, include

from comments import views
from rest_framework.routers import DefaultRouter


app_name = "comments"
router = DefaultRouter()

router.register("comments", views.CommentsViewSet)

urlpatterns = [path("", include(router.urls))]
