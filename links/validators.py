from rest_framework import serializers

import re

TEXT_NUMBERS_PATTERN = re.compile("[A-Za-z0-9]+")

class TitleValidator:

    def validate_title(self, value):
        if not TEXT_NUMBERS_PATTERN.fullmatch(value):
            raise serializers.ValidationError('Invalid format title, '\
                'do not use invalid characters')
        return value