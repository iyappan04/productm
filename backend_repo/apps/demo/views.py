# TODO There's certainly more than one way to do this task, so take your pick.

from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


from apps.demo.serializers import PostSerializer, CommentSerializer
from apps.demo.models import Post, Comment

from rest_framework.decorators import api_view

class MyCustomPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })


class PostsView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = MyCustomPagination
    
    # def list():

@api_view(['GET'])
def get_post(request, id):
    post = Post.objects.get(id=id)
    # comments = Comment.objects.filter(post=id)
    data = PostSerializer(post, many=False).data
    # order_by('-timestamp')[:3]

    # data = {
    #     "posts": PostSerializer(posts, many=False).data,
    #     "comments": CommentSerializer(comments, many=False).data
    # }
    return Response(data)

@api_view(['GET'])
def get_post_comments(request, id):
    comment = Comment.objects.filter(post = id).order_by('-timestamp')[:3]
    # Comment.objects.filter(post=id).order_by('?')[:3]
    data = CommentSerializer(comment, many=True).data
    return Response(data)