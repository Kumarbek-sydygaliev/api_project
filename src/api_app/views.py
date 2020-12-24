import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse 
from .models import Post, Tag
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import PostListSerializer, PostDetailSerializer

@api_view(['GET'])
def all_posts(request):
    posts = Post.objects.all()
    ser = PostListSerializer(posts, many=True)
    return Response(data=ser.data)

@api_view(['GET'])
def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    ser = PostDetailSerializer(post)
    return Response(data=ser.data)
