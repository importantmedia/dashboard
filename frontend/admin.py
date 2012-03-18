from django.contrib import admin
from frontend.models import AdFormat, Network, Publisher, Tag

class AdFormatAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ['ad_format_name', 'size']
admin.site.register(AdFormat, AdFormatAdmin)

class NetworkAdmin(admin.ModelAdmin):
    search_fields = ["network_name"]
    ordering = ["network_name"]
    exclude = ["supports_threshold", "us_only"]
    list_display = ['network_name', 'pay_type', 'enabled', 'us_only']
    list_editable = ['pay_type', 'enabled', 'us_only']
admin.site.register(Network, NetworkAdmin)

class PublisherAdmin(admin.ModelAdmin):
    search_fields = ["site_name"]
    ordering = ["site_name"]
    list_display = ['site_name', 'site_url']
admin.site.register(Publisher, PublisherAdmin)

class TagAdmin(admin.ModelAdmin):

    def tag_info(self, tag):
        out = "%s<br />%s" % (tag.tag_name, tag.size)
        return out
    tag_info.allow_tags = True
    tag_info.short_description = "Tag"
    tag_info.admin_order_field = 'tag_name'

    # freq, rej, sample, pacing, daily
    def delivery(self, tag):
        out = ""
        if tag.frequency_cap:
            out += "Frequency Cap: %s<br />" % tag.frequency_cap
        if tag.rejection_time:
            out += "Rejection Time: %s min<br />" % tag.rejection_time
        if tag.sample_rate:
            out += "Sample Rate: %s%%<br />" % tag.sample_rate
        if tag.pacing:
            out += "Pacing Rate: %s%%<br />" % tag.pacing
        return out
    delivery.allow_tags = True

    def clickable_publisher(self, tag):
        return '<a href="../publisher/%s">%s</a>' % (tag.publisher.id, tag.publisher.site_name)
    clickable_publisher.allow_tags = True
    clickable_publisher.short_description = "Publisher"

    def clickable_network(self, tag):
        return '<a href="../network/%s">%s</a>' % (tag.network.id, tag.network.network_name)
    clickable_network.allow_tags = True
    clickable_network.short_description = "Network"

    search_fields = ["tag_name", "publisher__site_name", "network__network_name", "tag"]
    list_filter = ["publisher", "network", "size", "enabled", "always_fill"]
    ordering = ["publisher", '-tier', 'value']
    list_editable = ['tier', 'value']
    list_display = ['tag_info', 'clickable_publisher', 'clickable_network', 'tier', 'value', "enabled", "always_fill", "floor", "delivery"]
admin.site.register(Tag, TagAdmin)
