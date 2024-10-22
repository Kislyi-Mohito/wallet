from django.db import models

class Wallet(models.Model):
    walletid = models.IntegerField(primary_key=True)  # Первый столбец
    balans = models.FloatField()  # Второй столбец, тип real в PostgreSQL

    class Meta:
        db_table = 'wallet_id'  # Имя вашей таблицы в базе данных

    def __str__(self):
        return f"Wallet ID: {self.walletid}, Balance: {self.balans}"