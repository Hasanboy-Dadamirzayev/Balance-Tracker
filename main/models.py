from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Tranzit(models.Model):
    amount = models.FloatField(validators=[MinValueValidator(0.0)])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20, choices=(('Income', 'Income'), ('Expense', 'Expense')))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} - {self.type}"

