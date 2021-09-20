from django.db import models

from django.utils.translation import ugettext_lazy as _

class Link(models.Model):

    title = models.CharField(max_length=32, unique=True)
    visits = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")

    def __str__(self):
        return self.title
