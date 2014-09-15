from taggit.models import Tag
from django.db.models import Count

def root(request):
    tags = Tag.objects.select_related('bug') \
        .annotate(c=Count('bug')).order_by('-c') \
        .all()
    print tags
