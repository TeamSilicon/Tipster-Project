from string import Template
import os
from django.conf import settings


def read_template(filename):
    file_path = os.path.join(settings.STATIC_ROOT, filename)
    template_file = open(file_path, mode="r", encoding="utf-8")
    template_content = template_file.read()
    return Template(template_content)
