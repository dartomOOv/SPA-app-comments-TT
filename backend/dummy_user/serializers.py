from rest_framework import serializers

from dummy_user.models import DummyUserModel


class DummyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyUserModel
        fields = (
            "id",
            "username",
            "email"
        )
