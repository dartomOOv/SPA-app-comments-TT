from rest_framework import serializers

from comments.models import CommentsModel
from dummy_user.models import DummyUserModel
from dummy_user.serializers import DummyUserSerializer


class CommentsSerializer(serializers.ModelSerializer):
    user = DummyUserSerializer()

    class Meta:
        model = CommentsModel
        fields = (
            "id",
            "user",
            "home_page",
            "text",
            "response_to",
            "amount_of_responses"
        )

    def create(self, validated_data):
        user_data = validated_data.pop("user")

        user = DummyUserModel.objects.create(**user_data)
        comment = CommentsModel.objects.create(**validated_data, user=user)

        return comment


class CommentRetrieveSerializer(CommentsSerializer):
    responses = CommentsSerializer(many=True)

    class Meta:
        model = CommentsModel
        fields = (
            "id",
            "user",
            "home_page",
            "text",
            "responses"
        )
