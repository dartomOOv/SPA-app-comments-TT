from rest_framework import serializers

from comments.models import CommentsModel
from dummy_user.serializers import DummyUserSerializer


class CommentsSerializer(serializers.ModelSerializer):
    user = DummyUserSerializer()

    class Meta:
        model = CommentsModel
        fields = (
            "id",
            "user",
            "home_page",
            "text"
        )
