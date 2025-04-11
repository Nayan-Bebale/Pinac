from django import template
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

register = template.Library()

@register.filter
def remove_query_param(url, param):
    """
    Remove a parameter from a URL's query string
    """
    parsed = urlparse(url)
    query_dict = parse_qs(parsed.query)
    
    if param in query_dict:
        del query_dict[param]
    
    return urlunparse(parsed._replace(query=urlencode(query_dict, doseq=True)))