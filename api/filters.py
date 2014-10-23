import django_filters
from robocrm.models import RoboUser
from channels.models import Channel
from rest_framework import generics

# TODO: clean this class up
class RoboUserFilter(django_filters.FilterSet):

  # Eliminates the need for user__ prefix in filter
  username = django_filters.CharFilter(name='user__username')
  email = django_filters.CharFilter(name='user__email')
  first_name = django_filters.CharFilter(name='user__first_name')
  last_name = django_filters.CharFilter(name='user__last_name')
  is_active = django_filters.BooleanFilter(name='user__is_active')
  date_joined = django_filters.DateTimeFilter(name='user__date_joined')
  last_login = django_filters.DateTimeFilter(name='user__last_login')

  # TODO: make static method
  def magnetic_filter(qs, value):
    if value:
      return qs.filter(magnetic__gt=0)
    else:
      return qs.exclude(magnetic__gt=0)

  # TODO: make static method
  def rfid_filter(qs, value):
    if value:
      return qs.filter(rfid__gt=0)
    else:
      return qs.exclude(rfid__gt=0)

  magnetic = django_filters.BooleanFilter(action=magnetic_filter)
  rfid = django_filters.BooleanFilter(action=rfid_filter)
    
  class Meta:
    model = RoboUser
    fields = ('id', )


class ChannelFilter(django_filters.FilterSet):

  # TODO: make static method
  def active_filter(qs, value):
    o = qs.all()
    for c in o:
      if c.active != value:
        qs = qs.exclude(id=c.id)
    return qs

  active = django_filters.BooleanFilter(action=active_filter)
    
  class Meta:
    model = Channel
    fields = ('id', 'name', 'created', 'updated', 'active')
