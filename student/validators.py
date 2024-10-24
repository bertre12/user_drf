from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image as PilImage


# Ограничение по размеру (например, 10MB).
def validate_image(image):
    max_size = 10 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError(_('Размер изображения не должен превышать '
                                '10MB.'))

    # Ограничение по формату.
    valid_formats = ['JPEG', 'PNG']
    image_file = PilImage.open(image)
    if image_file.format not in valid_formats:
        raise ValidationError(
            _('Формат изображения должен быть JPEG или PNG.'))
