from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from comments.models import CommentsModel
from comments.serializers import CommentsSerializer, CommentRetrieveSerializer


class CommentsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = CommentsModel.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action == "list":
            queryset =  queryset.filter(response_to__isnull=True)

        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CommentRetrieveSerializer

        return CommentsSerializer
