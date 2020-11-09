from rest_framework.routers import SimpleRouter
from .ViewSets import CategoryViewSet, BlogViewSet

api_router = SimpleRouter()
api_router.register("tag", CategoryViewSet, base_name="api-tag")
api_router.register("blog", BlogViewSet, base_name="api-blog")


urlpatterns = api_router.urls