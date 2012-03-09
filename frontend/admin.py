from django.contrib import admin
from frontend.models import AdFormat, Network, Publisher, Tag, TagOption, TagTarget

#class AdFormatAdmin(admin.ModelAdmin):
    #ordering = ["id"]
    #list_display = ['ad_format_name', 'size']
#admin.site.register(AdFormat, AdFormatAdmin)

class NetworkAdmin(admin.ModelAdmin):
    search_fields = ["network_name"]
    ordering = ["network_name"]
    list_display = ['network_name', 'pay_type', 'enabled']
admin.site.register(Network, NetworkAdmin)

class PublisherAdmin(admin.ModelAdmin):
    search_fields = ["site_name"]
    ordering = ["site_name"]
    list_display = ['site_name', 'site_url']
admin.site.register(Publisher, PublisherAdmin)

class TagAdmin(admin.ModelAdmin):
    search_fields = ["name", "publisher__name", "network__name", "code"]
    list_filter = ["publisher", "network", "size", "enabled", "always_fill"]
    ordering = ["publisher", '-tier', 'value']
    list_editable = ['tier', 'value', "floor", "rejection_time"]
    list_display = ['tag_name', 'publisher', 'network', 'size', 'tier', 'value', "enabled", "always_fill", "floor", "frequency_cap", "rejection_time", "sample_rate", "pacing", "max_daily_impressions"]
admin.site.register(Tag, TagAdmin)
