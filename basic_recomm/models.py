from django.db import models
from jsonfield import JSONField

class Font_keyword_value(models.Model):
    font_name=models.CharField(max_length=50)
    key_value=JSONField(default=dict)
