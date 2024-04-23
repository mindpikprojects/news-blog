from django.urls import path, include
from .views import (
    BlogApiView,
    BlogSearchApiView,
    CategoryApiView,
    CategoryPostApiView,
    PopularPostsApiView,
    TrendingPostsApiView,
    AdPostApiView,
    CatListApiView,
)
from rest_framework import routers

router = routers.SimpleRouter()
router.register("blogs", BlogApiView, basename="blogs")
router.register("blogsr", BlogSearchApiView, basename="blogsearch")
router.register("category", CategoryPostApiView, basename="category_id")
router.register("category", CategoryApiView, basename="category")

router.register("cat", CatListApiView, basename="cat")

router.register("popular", PopularPostsApiView, basename="popular")
router.register("trending", TrendingPostsApiView, basename="trending")
router.register("ads", AdPostApiView, basename="ads")

urlpatterns = [
    path("", include(router.urls)),
    # path("category/<int:pk>/", CategoryPostApiView.as_view({'get': 'retrieve'}), name="category_id"),

]
