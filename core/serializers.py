from rest_framework import serializers
from .models import Profile, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ('id', )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user', write_only=True, queryset=User.objects.all())

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ('id',)
