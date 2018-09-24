import logging

from .clients import Client, DummyClient
from .io import UrlFetcher, FileFetcher

log = logging.getLogger(__name__)


def client(
    url='',
    headers=None,
    refresh_interval=60,
    fetch=None,
    *al,
    **kw
):
    if fetch:
        pass
    elif not url:
        return DummyClient()
    elif ':' not in url:
        fetch = FileFetcher(url)
    elif url.startswith('file:///'):
        fetch = FileFetcher(url[8:])
    elif url.startswith('http://') or url.startswith('https://'):
        fetch = UrlFetcher(url + '/api/client/features', refresh_interval, headers)
    else:
        log.error("Unexpected unleash client url scheme: %r", url)
        raise ValueError(url)

    return Client(url, headers, *al, fetch=fetch, **kw)
