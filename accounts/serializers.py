from rest_framework import serializers

from accounts.models import Accounts

class AccountRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Accounts
        fields = ['email','first_name','last_name','number','password','password2','waiver']
        extar_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Accounts(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            number=self.validated_data['number'],
            waiver=self.validated_data['waiver'],
            
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'passwords do not match'})
        account.set_password(password)
        account.save()
