from django.db import models

class Publications(models.Model):
    title = models.CharField('Назва', max_length=60)  # Назва публікації
    full_text = models.TextField('Стаття')  # Текст публікації
    date = models.DateTimeField(auto_now_add=True)  # Дата публікації

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'  # Ім'я для одного запису
        verbose_name_plural = 'Новини'  # Ім'я для групи записів

class Forum_Publications(models.Model):
    title = models.CharField('Назва', max_length=60)  # Назва запису на форумі
    full_text = models.TextField('Стаття')  # Текст запису на форумі
    date = models.DateTimeField(auto_now_add=True)  # Дата публікації

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запис'  # Ім'я для одного запису
        verbose_name_plural = 'Записи'  # Ім'я для групи записів
