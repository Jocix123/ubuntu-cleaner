from ubuntucleaner.utils import system
from ubuntucleaner.janitor import JanitorCachePlugin


class ThumbnailCachePlugin(JanitorCachePlugin):
    __title__ = _('Thumbnail cache')
    __category__ = 'personal'

    if system.CODENAME in ['precise']:
        root_path = '~/.thumbnails'
    else:
        root_path = '~/.cache/thumbnails'
