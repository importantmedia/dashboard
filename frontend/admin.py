from django.contrib import admin
from frontend.models import AdFormat, Network, Publisher, Tag, TagOption, TagTarget

class AdFormatAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ['ad_format_name', 'size']
admin.site.register(AdFormat, AdFormatAdmin)


class NetworkAdmin(admin.ModelAdmin):
    search = ["network_name"]
    ordering = ["network_name"]
    list_display = ['network_name', 'pay_type', 'enabled']
admin.site.register(Network, NetworkAdmin)

class PublisherAdmin(admin.ModelAdmin):
    search = ["site_name"]
    ordering = ["site_name"]
    list_display = ['site_name', 'site_url']
admin.site.register(Publisher, PublisherAdmin)

class TagAdmin(admin.ModelAdmin):
    ordering = ["publisher", '-tier', 'value']
    list_display = ['tag_name', 'publisher', 'network', 'value']
admin.site.register(Tag, TagAdmin)
