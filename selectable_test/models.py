# -*- encoding: utf-8 -*-
import uuid
from django.core import urlresolvers
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class BaseModel(models.Model):
    """
    Base class for all models;
    defines common metadata
    """
    class Meta:
        abstract = True

    # Primary key
    id = models.UUIDField('id', default=uuid.uuid4, primary_key=True, unique=True, null=False, blank=False, editable=False)
    description = models.CharField('description', max_length=256, null=False, blank=True)

    def __str__(self):
        if self.description:
            return self.description
        return str(self.id)

    def get_admin_url(self):
        return urlresolvers.reverse("admin:%s_%s_change" %
            (self._meta.app_label, self._meta.model_name), args=(self.id,))


class Country(BaseModel):

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class City(BaseModel):

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    country = models.ForeignKey(Country, null=True, blank=True)


class Machine(BaseModel):
    country = models.ForeignKey(Country, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    address = models.TextField('address', null=False, blank=True)

