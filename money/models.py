import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Income(BaseModel):
    SALARY = 'SALARIO'
    OTHER = 'OUTRO'

    ORIGIN_CHOICES = [
        (SALARY, 'Salário'),
        (OTHER, 'Outro'),
    ]

    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )
    date = models.DateField(default=timezone.now().replace(day=1))
    description = models.CharField(max_length=100, null=False, blank=False)
    origin = models.CharField(
        max_length=10, choices=ORIGIN_CHOICES, default=SALARY
    )

    def __str__(self):
        return f"R${self.value} - {self.date.strftime('%B/%Y')}"

    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'
        indexes = [
            models.Index(fields=['value', 'date']),
        ]


class Payment(BaseModel):
    name = models.CharField(max_length=50, null=False, blank=False)
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )
    due_date = models.DateField(default=timezone.now)
    pay = models.BooleanField(default=False)
    payment_date = models.DateField(null=True)

    def is_overdue(self):
        return timezone.now().date() > self.due_date

    def days_until_due(self):
        return (self.due_date - timezone.now().date()).days

    def __str__(self):
        return f"{self.name} - {self.due_date.strftime('%B/%Y')}"

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        indexes = [
            models.Index(fields=['value', 'due_date']),
        ]
