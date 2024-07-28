from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Equipment, InventoryChange
from .forms import EquipmentForm, UpdateQuantityForm,UserRegistrationForm
from django.http import HttpResponseForbidden
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import UserEditForm
from django.urls import reverse

def home(request):
    return render(request, 'equipment/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.is_staff = form.cleaned_data.get('is_staff')
            user.is_superuser = form.cleaned_data.get('is_superuser')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('equipment_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment/equipment_list.html', {'equipments': equipments})

@login_required
def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == "POST":
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        form = UpdateQuantityForm(request.POST, instance=equipment)
        if form.is_valid():
            old_quantity = equipment.quantity
            form.save()
            new_quantity = form.cleaned_data['quantity']
            InventoryChange.objects.create(
                equipment=equipment,
                user=request.user,
                old_quantity=old_quantity,
                new_quantity=new_quantity
            )
            return redirect('equipment_list')
    else:
        form = UpdateQuantityForm(instance=equipment)
    changes = InventoryChange.objects.filter(equipment=equipment).order_by('-timestamp')
    return render(request, 'equipment/equipment_detail.html', {'equipment': equipment, 'form': form, 'changes': changes})

@login_required
def add_equipment(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'equipment/add_equipment.html', {'form': form})

@login_required
def edit_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == "POST":
        form = EquipmentForm(request.POST, request.FILES, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_detail', pk=equipment.pk)  # リダイレクト先のURLパターンを確認
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'equipment/edit_equipment.html', {'form': form, 'equipment': equipment})

@login_required
def user_list(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    users = User.objects.all()
    return render(request, 'equipment/user_list.html', {'users': users})

@login_required
def edit_user(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'equipment/edit_user.html', {'form': form})
