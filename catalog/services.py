from django.conf import settings
from django.core.cache import cache

from catalog.models import Version


def get_cached_versons_for_product(product_pk):
    if settings.CACHE_ENABLED:
        key = f'version_list_{product_pk}'
        version_list = cache.get(key)
        if version_list is None:
            version_list = Version.objects.filter(product__pk=product_pk)
            cache.set(key, version_list)
    else:
        version_list = Version.objects.filter(product__pk=product_pk)

    return version_list
