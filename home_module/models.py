from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=128, verbose_name='نام و نام خانوادگی')
    phone = models.CharField(max_length=255, unique=True, verbose_name='تلفن همراه')
    message = models.TextField(max_length=5000, verbose_name='متن پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    is_red = models.BooleanField(default=False, verbose_name='خوانده شده / خوانده نشده')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'ارتباط با ما'