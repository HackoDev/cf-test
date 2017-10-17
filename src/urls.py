from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from cf_core.router import router
from cf_core.api import (
    DictionaryViewSet, ModerationNoteViewSet
)

from cf_users.api import (
    UserProfileViewSet, PublishedProfileVewSet
)
from cf_adverts.api import (
    AdvertViewSet, EstimateViewSet, EventsViewSet
)

router.register('profiles', UserProfileViewSet, base_name='profiles')
router.register('published-profiles', PublishedProfileVewSet,
                base_name='published-profiles')

router.register('dictionaries', DictionaryViewSet, base_name='dictionaries')

router.register('adverts', AdvertViewSet, base_name='adverts')
router.register('moderation-notes', ModerationNoteViewSet, base_name='notes')
router.register('estimates', EstimateViewSet, base_name='estimates')
router.register('events', EventsViewSet, base_name='events')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls', namespace='jet')),
    url(r'^api/v1/', include(router.get_urls(), namespace='api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
