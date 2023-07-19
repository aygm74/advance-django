from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from .serializer import CategorySerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from rest_framework import viewsets

from ...models import Category, Posts

"""function based view"""

# @api_view(["GET","POST"])
# @permission_classes([IsAuthenticated])
# def postList(request):
#     if request.method =="GET":
#         comment=posts.objects.all()
#         # comment=get_object_or_404(posts,pk=id)
#         post_serializer=PostSerializer(comment,many=True)
#         return Response(post_serializer.data)
#     elif request.method== "POST":
#         serializer=PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(request.data)


# @api_view(["GET","PUT","Delete"])
# def postDetail(request,id):
#     comment=get_object_or_404(posts,pk=id,status=True)
#     if request.method =="GET":
#         serializer=PostSerializer(comment)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer=PostSerializer(comment,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         comment.delete()
#         return Response({"data" :"data delete successfully"},status=204)


"""  class based API view   """
'''class PostListApi(APIView):
    """ retreveing list of post"""

    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer

    def get(self,request):
        comment=posts.objects.all()
        post_serializer=PostSerializer(comment,many=True)
        return Response(post_serializer.data)

    """ creating post with provided data"""
    def post(self, request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data)

""" get and update or delete post////ApiVeiw PostDetail """
class PostDetailApi(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class=PostSerializer

    def get(self,request,id):
        comment=get_object_or_404(posts,pk=id)
        serializer= self.serializer_class(comment)
        return Response(serializer.data)

    def put(self,request,id):
        comment=get_object_or_404(posts,pk=id)
        serializer=PostSerializer(comment,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        comment=get_object_or_404(posts,pk=id)
        serializer=PostSerializer(comment,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.delete()
        return Response({"data" :"data delete successfully"},status=204)












""" Generic Api view """
""" get and list post////ApiVeiw Mixin Postlist """
class PostListApi(GenericAPIView , ListModelMixin,CreateModelMixin):
    """ retreveing list of post"""

    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer
    queryset=posts.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

'''
""" get and update or delete post////ApiVeiw Mixin PostDetail """
# class PostDetailApi(GenericAPIView,
#                     RetrieveModelMixin,
#                     DestroyModelMixin,
#                     UpdateModelMixin):
#     permission_classes=[IsAuthenticated]
#     serializer_class=PostSerializer
#     queryset=posts.objects.filter(status=True)
#     # lookup_field="id" ''' find id word in url otherwise default is pk in url so change the url'''

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

""" get and update or delete post////ApiVeiw PostDetail """
# class PostDetailApi():
#     permission_classes=[IsAuthenticated]
#     serializer_class=PostSerializer
#     queryset=posts.objects.filter(status=True)
#     # lookup_field="id" ''' find id word in url otherwise default is pk in url so change the url'''

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)


"""generic apiView for PostlistView"""
# class PostListApi(ListCreateAPIView):
#     """ retreveing list of post and create post"""
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     serializer_class=PostSerializer
#     queryset=posts.objects.all()

"""generic apiView for PostDetailView"""
# class PostDetailApi(RetrieveUpdateDestroyAPIView):
#      permission_classes=[IsAuthenticated]
#      serializer_class=PostSerializer
#      queryset=posts.objects.filter(status=True)


""" viewsets class based"""
# class PostViewSet(viewsets.ViewSet):
#     permission_classes=[IsAuthenticated]
#     serializer_class=PostSerializer
#     queryset=posts.objects.all()

#     def list(self,request,*args,**kwargs):
#         serializer=self.serializer_class(self.queryset,many=True)
#         return Response(serializer.data)

#     def retrieve(self,request,pk=None,*args,**kwargs):
#         comment=get_object_or_404(self.queryset,pk=pk)
#         serializer=self.serializer_class(comment)
#         return Response(serializer.data)

"""modelviewset class based view"""


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Posts.objects.all()

    @action(methods=['get'],detail=False,url_path='select-list',url_name='select')
    def select(self, request, *args, **kwargs):
        return Response('ok')


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    search_fields = ['username', 'email']