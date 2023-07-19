from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import PostViewSet, CategoryViewSet

# from rest_framework.documentation import include_docs_urls


router = DefaultRouter()
router.register('post', PostViewSet, basename='post')
router.register('category', CategoryViewSet, basename='category')

# router.register('post', PostViewSet, basename='post')  # post-detail
# router.register('category', CategoryViewSet, basename='category')

# urlpatterns=router.urls
app_name = "api-v1"

urlpatterns = [  # # path('post/',postList,name='postList'),
    #     # path('post/<id>/',postDetail,name='postDetail'),
    #     # path('post/',PostListApi.as_view(),name='postList'),
    #     # path('post/<int:pk>',PostDetailApi.as_view(),name='postDetail'),
    #     # path('post/',PostViewSet.as_view({'get':'list'}),name='post-list'),
    #     # path('post/<int:pk>',PostViewSet.as_view({'get':'retrieve'}),name='post-detail')

    # path('',include('api-doc',include_docs_urls(title='api-sample')))
]
urlpatterns += router.urls
