from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www.kirr.com:8000/kirr'),
    host(r'(?!www).*', 'juno.hostsconf.urls', name='wildcard'),
)