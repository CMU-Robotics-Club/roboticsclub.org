from django.contrib import admin
from .models import Channel
from crm.admin import UpdatedByAdmin

class ChannelAdmin(UpdatedByAdmin):
  fields = ('id', 'name', 'value', 'created_datetime', 'updated_datetime', 'active', 'updater_url', )
  readonly_fields = ['id', 'active', 'created_datetime', 'updated_datetime', 'updater_url', ]
  list_display = ('id', 'name', 'value', 'created_datetime', 'updated_datetime', 'active', 'updater_url', )

  def save_model(self, request, obj, form, change):
    obj.updater_object = request.user
    obj.save()

  def get_readonly_fields(self, request, obj=None):
    if obj:
      return super().get_readonly_fields(request, obj) + ['name']
    else:
      return super().get_readonly_fields(request, obj)

admin.site.register(Channel, ChannelAdmin)