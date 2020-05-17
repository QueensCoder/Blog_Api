from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = (
            'updated_at',
        )
        model = Post
