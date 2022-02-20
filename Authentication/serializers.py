from rest_framework import serializers
from .models import User, Usertypes
from rest_framework.validators import UniqueValidator
# from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    """Serializers userserializer requests and creates a new user."""

    # Ensure email is provided and is unique
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='This email is already used by another user',
            )
        ],
        error_messages={
            'required': 'Email is required',
        }
    )

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.RegexField(
        regex="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
        max_length=128,
        min_length=8,
        write_only=True,
        required=False,
        error_messages={
            'required': 'Password is required',
            'invalid': 'Password must have a number and a letter',
            'min_length': 'Password must have at least 8 characters',
            'max_length': 'Password cannot be more than 128 characters'
        }
    ),
    # iscustomer = serializers.BooleanField(required=False)
    # branchid = serializers.IntegerField(required=False)

    # hubid = serializers.IntegerField(required=False)
    
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'password',
            'usertype',
            'passportno',
            'phone'
        )
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            usertype=validated_data['usertype'],
            passportno=validated_data['passportno'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        # Token.objects.create(user=user)
        print(user)
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usertypes
        fields = '__all__'