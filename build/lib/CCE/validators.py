from schematics.models import Model
from schematics.types import StringType


class CCEItem(Model):
    image = StringType(required=True)
    title = StringType(required=True)
    author = StringType(required=True)
    date = StringType(required=True)
    text = StringType(required=True)
