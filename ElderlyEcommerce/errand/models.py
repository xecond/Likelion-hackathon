from django.db import models
from django.utils import timezone
from account.models import CustomUser

class Errand(models.Model):
    STATUS_CHOICES = [
        ('pending', '수락 대기'),
        ('in_progress', '진행 중'),
        ('completed', '완료'),
    ]
    item = models.CharField(max_length=300)
    address_1 = models.CharField(max_length=500)
    address_2 = models.CharField(max_length=500)
    client = models.ForeignKey(CustomUser, related_name='requested_errands', on_delete=models.CASCADE, null=True, blank=True)
    server = models.ForeignKey(CustomUser, related_name='accepted_errands', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='수락 대기')

    def __str__(self):
        return f"{self.item} - {self.get_status_display()}"