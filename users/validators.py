from django.contrib.auth.password_validation import MinimumLengthValidator, CommonPasswordValidator, \
    NumericPasswordValidator, UserAttributeSimilarityValidator
from django.core.exceptions import ValidationError


class PLMinimumLengthValidator(MinimumLengthValidator):
    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError as e:
            raise ValidationError("Hasło jak siusiaczek, lepiej żeby było dłuższe (min. %(min_length)d znaków).",
                                  code=e.code, params=e.params)


class PLCommonPasswordValidator(CommonPasswordValidator):
    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError as e:
            raise ValidationError("Hasło to nie influencer, nie może być popularne.",
                                  code=e.code, params=e.params)


class PLNumericPasswordValidator(NumericPasswordValidator):
    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError as e:
            raise ValidationError("Hasło to nie jest misiu Twoj pin do karty, nie mogą być same cyfry.",
                                  code=e.code, params=e.params)


class PLUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError as e:
            raise ValidationError("Hasło jest zbyt podobne do danych konta.",
                                  code=e.code, params=e.params)
