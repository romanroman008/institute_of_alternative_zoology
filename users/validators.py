from django.contrib.auth.password_validation import MinimumLengthValidator, CommonPasswordValidator, \
    NumericPasswordValidator, UserAttributeSimilarityValidator
from django.core.exceptions import ValidationError


class PLMinimumLengthValidator(MinimumLengthValidator):
    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError as e:
            raise ValidationError("Hasło powinno mieć minimum %(min_length)d znaków.",
                                  code=e.code, params=e.params)


class PLCommonPasswordValidator(CommonPasswordValidator):
    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError as e:
            raise ValidationError("Hasło zbyt popularne.",
                                  code=e.code, params=e.params)


class PLNumericPasswordValidator(NumericPasswordValidator):
    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError as e:
            raise ValidationError("Hasło nie może składać się z samych cyfr.",
                                  code=e.code, params=e.params)


class PLUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError as e:
            raise ValidationError("Hasło jest zbyt podobne do danych konta.",
                                  code=e.code, params=e.params)
