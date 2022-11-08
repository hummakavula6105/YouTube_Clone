from rest_framework import serializers
from comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'make', 'model', 'year', 'user_id']
        depth = 1
