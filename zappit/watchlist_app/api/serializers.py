from rest_framework import serializers
from ..models import Movie, WatchList, StreamPlatform, Review


# def active_is_true(value):
#     if value == False:
#         raise serializers.ValidationError("Activate is false!")
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField(validators=[active_is_true])
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     # Walidacja całego obiektu
#     def validate(self, data):
#         if len(data['description']) < 2:
#             raise serializers.ValidationError("Description is to short!")
#         else:
#             return data
#
#     # Walidacja tylko pola
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is to short!")
#         else:
#             return value


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['active']

    def get_len_name(self, object):
        return len(object.name)

    # Walidacja całego obiektu
    def validate(self, data):
        if len(data['description']) < 2:
            raise serializers.ValidationError("Description is to short!")
        else:
            return data

    # Walidacja tylko pola
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is to short!")
        else:
            return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # One to meny
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['active']


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    # watchlist = serializers.StringRelatedField(many=True, read_only=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="movie-details-v4")
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
