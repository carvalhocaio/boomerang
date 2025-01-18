from django.contrib import admin

from .models import Income, Payment


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('value', 'date', 'description', 'origin')
    search_fields = ('origin',)
    list_filter = ('date', 'origin')
    ordering = ('-date',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'value',
        'due_date',
        'pay',
        'payment_date',
        'is_overdue_label',
        'days_until_due',
    )
    search_fields = ('nome', 'value')
    list_filter = ('due_date', 'pay')
    ordering = ('-due_date',)

    def is_overdue_label(self, obj):
        if obj.pay:
            return ''
        return 'Late' if obj.is_overdue() else 'On Deadline'

    is_overdue_label.short_description = 'status'

    def days_until_due(self, obj):
        if obj.pay:
            return ''
        days = obj.days_until_due()
        return f'{days} days' if days >= 0 else f'{-days} days late'

    days_until_due.short_description = 'Days until winning'
