from rest_framework import serializers
from .models import SubReddits,Subscriptions,Posts,Comments,Votes

class SubRedditsSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','name','description','created_at')
        model=SubReddits
class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','user_id','Boards_id')
        model=Subscriptions
class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','board','text','detail','created_at','author')
        model=Posts
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','from_user','post_id','text','created_at')
        model=Comments
class VotesSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','from_id','comment_id','post_id','value')
        model=Votes