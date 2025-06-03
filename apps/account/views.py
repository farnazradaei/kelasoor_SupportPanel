from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import Group
from .models import User, OTP
import random
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from kavenegar import KavenegarAPI, APIException, HTTPException
import uuid





class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            role = request.data.get('role', 'user')  # گروه پیش‌فرض user
            if role in ['user', 'support', 'superuser']:
                group, _ = Group.objects.get_or_create(name=role)
                user.groups.add(group)
            if role == 'superuser':
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)




def send_otp_sms(phone, message):
    try:
        api = KavenegarAPI('YOUR_API_KEY37316A4A677756394D5649486C44516D5557413255517857776F704349536D694B2F5275562F76305569593D_HERE')  # کلید واقعی‌ات را اینجا بذار
        params = {
            'sender': '2000660110',
            'receptor': phone,
            'message': message,
        }
        api.sms_send(params)
        return True
    except (APIException, HTTPException) as e:
        print(f"Error sending SMS: {e}")
        return False


class SendOTPView(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        if not phone:
            return Response({"detail": "Phone number is required."}, status=status.HTTP_400_BAD_REQUEST)

        code = str(random.randint(100000, 999999))

        user, created = User.objects.get_or_create(phone_number=phone)

        OTP.objects.create(user=user, code=code, is_used=False)

        message = f"کد تایید شما: {code}"

        if send_otp_sms(phone, message):
            return Response({"detail": "OTP sent successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Failed to send OTP."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VerifyOTPView(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        code = request.data.get("code")

        if not phone or not code:
            return Response({"detail": "Phone and code are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone ,
                defaults={
                    "national_id": str(uuid.uuid4()),  
                    "password": User.objects.make_random_password()  

                                    
                                    } )
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        otp = OTP.objects.filter(user=user, code=code, is_used=False).last()
        if otp and otp.is_valid():
            otp.is_used = True
            otp.save()

            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }, status=status.HTTP_200_OK)

        return Response({"detail": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)
