from __future__ import unicode_literals

import operator
from django.db.models import Q
# from django.contrib.auth import get_user_model
# User = get_user_model()

from selectable.registry import registry
from selectable.base import LookupBase
from selectable.base import ModelLookup
from .utils import prettyprint_queryset
from .utils import trace

from .models import Country
from .models import City


class ModelLookupEx(ModelLookup):

    def update_filters(self, request):
        pass

    def get_query(self, request, term):
        self.update_filters(request)
        qs = self.get_queryset()
        if term:
            search_filters = []
            if self.search_fields:
                for field in self.search_fields:
                    search_filters.append(Q(**{field: term}))
            qs = qs.filter(reduce(operator.or_, search_filters))
        prettyprint_queryset(qs)
        trace('results count: %d' % qs.count())
        return qs

    # def get_item(self, value):
    #     trace(['value:', value])
    #     obj = self.model.objects.get(id=value)
    #     return value

    # def get_item_label(self, item):
    #     return str(item.description)

    # def get_item_id(self, item):
    #     import ipdb; ipdb.set_trace()
    #     return str(item.id)

    # def get_item_value(self, item):
    #     return str(item.description)


class CountryLookup(ModelLookupEx):
    model = Country
    search_fields = ('description__icontains', )
    #filters = {'abilitato': True}

registry.register(CountryLookup)


class CityLookup(ModelLookupEx):
    model = City
    search_fields = ('description__icontains', )

    def update_filters(self, request):
        self.filters['country_id'] = request.GET.get('country_id', None)

registry.register(CityLookup)
