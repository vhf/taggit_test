from taggit.models import Tag
from django.db.models import Count
from bug.models import Bug


def root(request):
    b1, b2 = Bug(), Bug()
    b1.save()
    b2.save()
    b1.tags.add('tag1')
    b1.tags.add('tag2')
    b2.tags.add('tag1')

    tags = Tag.objects.select_related('bug') \
        .annotate(c=Count('bug')).values('c', 'name').order_by('-c') \
        .all()
    print tags
