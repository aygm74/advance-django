from rest_framework import serializers
from advance__django.models import Comments, Category


# class PostSerializer(serializers.Serializer):
#     title=serializers.CharField()
#     email=serializers.EmailField()
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Comments
        fields = ['title', 'relative_url', 'absolute_url', 'email', 'description', 'snippet', 'category']

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        pk = request.parser_context.get('kwargs').get('pk')
        if pk is None:
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
        else:
            rep
            """میاد می بینه اگه اسنیپت وجود داشت حذف میکنه در غیر اینصورت هیچی و اینکار را فقط برای لیست انجام میدهد"""
        rep['category'] = CategorySerializer(instance.category, context={'request': request}).data
        """اگر می خواهی سریالایزر از داخل سریالایزر دیگه ضدا بزنی حتما ریکوست باش بفرست زیر اگر to_representation داشتی درون سریالایزر دیگه  context را نمی تواند تشخیص دهد"""
        """مشکل این کار اینه که ما اگر اسنیپت پاپ کردیم در لیست ها هم پاپ می شود برای حل این مشکل از request کمک می گیریم"""
        return rep
