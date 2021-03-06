from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')
        # pk = serializers.IntegerField(read_only=True)
        # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
        # code = serializers.CharField(style={'base_template': 'textarea.html'})
        # linenos = serializers.BooleanField(required=False)
        # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
        # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
        #
        # def create(self, validated_data):
        #     """
        #     검증한 데이터로 새 'Snippet' 인스턴스를 생성하여 리턴한다
        #     """
        #     return Snippet.objects.create(**validated_data)
        #
        # def update(self, instance, validated_data):
        #     """
        #     검증한 데이터로 기존 'Snippet'인스턴스를 업데이트 한 후 리턴한다
        #     """
        #     instance.title = validated_data.get('title', instance.title)
        #     instance.code = validated_data.get('code', instance.code)
        #     instance.linenos = validated_data.get('linenos', instance.linenos)
        #     instance.language = validated_data.get('language', instance.language)
        #     instance.style = validated_data.get('style', instance.style)
        #     instance.save()
        #     return instance
