from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	is_auther = models.BooleanField(default=False,verbose_name='وضعیت نویسنگی')
	special_user = models.DateTimeField(default=timezone.now, verbose_name='زمان کاربری ویژه')

	def is_special_user():
		if self.special_user > timezone.now():
			return True
		else:
			return False