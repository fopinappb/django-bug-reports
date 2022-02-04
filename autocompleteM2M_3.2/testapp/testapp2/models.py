from django.db import models
from testapp import models as t_models


class Finding(t_models.Finding):
    extra = models.CharField(max_length=200)
