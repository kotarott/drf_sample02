from rest_framework import serializers
from news.models import Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DataTimeField(read_only=True)
    updated_at = serializers.DataTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Article.objrcts.create(**validated_data)

    def update(self, instance, validated_date):
        instance.author = validated_data.get('author', insance.author)
        instance.title = validated_data.get('title', insance.title)
        instance.description = validated_data.get('description', insance.description)
        instance.body = validated_data.get('body', insance.body)
        instance.location = validated_data.get('location', insance.location)
        instance.publication_date = validated_data.get('publication_date', insance.publication_date)
        instance.active = validated_data.get('active', insance.active)
        instance.save()
        return instance