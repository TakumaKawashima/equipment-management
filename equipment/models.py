from django.db import models
from django.contrib.auth.models import User

class Equipment(models.Model):
    name = models.CharField("名前", max_length=100)
    category = models.CharField("カテゴリ", max_length=100)
    status = models.CharField("状態", max_length=100)
    location = models.CharField("設置場所", max_length=100)
    description = models.TextField("説明")
    image = models.ImageField("画像", upload_to='equipment_images/', null=True, blank=True)
    quantity = models.PositiveIntegerField("在庫数", default=1)

    def __str__(self):
        return self.name

class InventoryChange(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    old_quantity = models.PositiveIntegerField()
    new_quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp.strftime('%Y年%m月%d日%H:%M')} - {self.user.username}: {self.new_quantity} に変更"
