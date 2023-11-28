# api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer

class CommentAPIView(APIView):
    def get(self, request, movie_id):
        comments = Comment.objects.filter(movie_id=movie_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
