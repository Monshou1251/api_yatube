from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    character_quantity = serializers.SerializerMethodField()
    publication_date = serializers.DateTimeField(source='pub_date', read_only=True)
    group = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Group.objects.all(),
        required=False
    )

    class Meta:
        fields = ('id', 'text', 'author', 'image',
                  'character_quantity', 'publication_date', 'group')
        read_only_fields = ('author',)
        model = Post

    def get_character_quantity(self, obj):
        return len(obj.text)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    character_quantity = serializers.SerializerMethodField()
    publication_date = serializers.DateTimeField(source='created',
                                                 read_only=True)
    class Meta:
        model = Comment
        fields = ('author', 'post', 'text', 'description', 'publication_date')