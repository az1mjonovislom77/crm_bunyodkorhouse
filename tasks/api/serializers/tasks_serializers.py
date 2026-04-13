from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from common.base.serializers_base import BaseReadSerializer
from tasks.models import Card, Project, Comment
from user.api.serializers.user_serializers import UserMiniSerializer


class CardSerializer(BaseReadSerializer):
    created_by = UserMiniSerializer(read_only=True)
    updated_by = UserMiniSerializer(read_only=True)

    class Meta(BaseReadSerializer.Meta):
        model = Card
        read_only_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user

        return Card.objects.create(**validated_data)


class CommentSerializer(BaseReadSerializer):
    created_by = UserMiniSerializer(read_only=True)
    updated_by = UserMiniSerializer(read_only=True)

    class Meta(BaseReadSerializer.Meta):
        model = Comment
        read_only_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']

    def create(self, validated_data):
        user = self.context['request'].user

        return Comment.objects.create(created_by=user, **validated_data)


class ProjectGetSerializer(serializers.ModelSerializer):
    users_full_name = SerializerMethodField()
    card_title = serializers.CharField(source='card.title', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    created_by = UserMiniSerializer(read_only=True)
    updated_by = UserMiniSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'users', 'description', 'comments', 'users_full_name', 'card', 'card_title', 'title',
                  'created_at')
        read_only_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']

    def get_users_full_name(self, obj):
        return [user.full_name for user in obj.users.all()]


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('users', 'description', 'card', 'title')
        read_only_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']

    def create(self, validated_data):
        users = validated_data.pop('users', [])
        project = Project.objects.create(**validated_data)

        if users:
            project.users.set(users)

        return project
