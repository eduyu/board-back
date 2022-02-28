from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    class CommentListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('user', 'content', 'created_at', 'updated_at')

    comments = CommentListSerializer(many=True)

    class Meta:
        model = Article
        fields = ('user', 'title', 'content', 'created_at', 'updated_at', 'comments',)


class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer()

    class Meta:
        model = Article
        fields = ('user', 'title', 'created_at',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'article', 'content')