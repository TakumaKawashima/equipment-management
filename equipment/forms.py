from django import forms
from .models import Equipment, OrderRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'category', 'status', 'location', 'description', 'image', 'quantity']
        labels = {
            'name': '名前',
            'category': 'カテゴリ',
            'status': '状態',
            'location': '設置場所',
            'description': '説明',
            'image': '画像',
            'quantity': '在庫数',
        }

    def __init__(self, *args, **kwargs):
        super(EquipmentForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='メールアドレス')
    is_staff = forms.BooleanField(required=False, label='スタッフとして登録する')
    is_superuser = forms.BooleanField(required=False, label='管理者として登録する')


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'ユーザー名',
            'password1': 'パスワード',
            'password2': 'パスワード（確認用）',
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'ユーザー名'
        self.fields['password1'].label = 'パスワード'
        self.fields['password2'].label = 'パスワード（確認用）'

class UpdateQuantityForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['quantity']
        labels = {
            'quantity': '在庫数',
        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_superuser']
        labels = {
            'username': 'ユーザー名',
            'email': 'メールアドレス',
            'is_staff': 'スタッフ',
            'is_superuser': '管理者',
        }

class OrderRequestForm(forms.ModelForm):
    class Meta:
        model = OrderRequest
        fields = ['quantity_requested']
        labels = {
            'quantity_requested': '発注数'
        }

class OrderRequestApprovalForm(forms.ModelForm):
    class Meta:
        model = OrderRequest
        fields = ['approved']
