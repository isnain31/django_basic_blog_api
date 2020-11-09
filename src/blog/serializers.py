from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    ModelSerializer
)
from .models import Category,Blog


class CategorySerializer(HyperlinkedModelSerializer):
    """Serialize Category data"""

    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-tag-detail",
            }
        }


class BlogSerializer(HyperlinkedModelSerializer):
    """Serialize Blog data"""

    categories = HyperlinkedRelatedField(
        lookup_field="slug",
        many=True,
        read_only=True,
        view_name="api-tag-detail",
    )

    class Meta:
        model = Blog
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-blog-detail",
            }
        }