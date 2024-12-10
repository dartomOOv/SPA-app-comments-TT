from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from comments.models import CommentsModel
from comments.serializers import CommentsSerializer


class CommentsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    queryset = CommentsModel.objects.all()
    serializer_class = CommentsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action == "list":
            queryset =  queryset.filter(response_to__isnull=True)

        return queryset
