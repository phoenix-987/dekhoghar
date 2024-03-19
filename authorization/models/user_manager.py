from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, name, is_owner, password=None, confirm_password=None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            is_owner=is_owner
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, is_owner=False, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            name=name,
            is_owner=is_owner,
            password=password
        )

        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user
