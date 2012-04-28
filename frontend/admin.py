from django.contrib import admin
from django.contrib.sites.models import Site
from frontend.models import Network, Publisher, Tag, TagTarget
from util import filldata_by_tag

# Get rid of the default django "site" admin, it's confusing
admin.site.unregister(Site)


class NetworkAdmin(admin.ModelAdmin):
    search_fields = ["network_name"]
    ordering = ["network_name"]
    exclude = ["supports_threshold", "us_only", "tag_template"]
    list_display = ['network_name', 'pay_type', 'enabled', 'brand_safety_level']
    list_editable = ['pay_type', 'enabled']
admin.site.register(Network, NetworkAdmin)


class PublisherAdmin(admin.ModelAdmin):
    exclude = ["beacon_throttle"]
    list_display = ['site_name', 'id', 'brand_safety_level', 'site_url']
    ordering = ["site_name"]
    search_fields = ["site_name"]
admin.site.register(Publisher, PublisherAdmin)


class TagTargetInline(admin.TabularInline):
    model = TagTarget
    extra = 1

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

        for targeting_criteria in tag.tagtarget_set.get_query_set().all():
            out += "%s: %s<br />" % (targeting_criteria.display_name(), targeting_criteria.key_value)
        return out
    delivery.allow_tags = True

    def clickable_publisher(self, tag):
        return '<a href="../publisher/%s">%s</a>' % (tag.publisher.id, tag.publisher.site_name)
    clickable_publisher.allow_tags = True
    clickable_publisher.short_description = "Publisher"

    def clickable_network(self, tag):
        out = '<a href="../network/%s">%s</a>' % (tag.network.id, tag.network.network_name)
        if tag.always_fill:
            out += "<br />Always fill"
        return out
    clickable_network.allow_tags = True
    clickable_network.short_description = "Network"

    def fillrate_stats(self, tag):
        stats = filldata_by_tag(tag.id)
        return "%s of %s filled, %s%%" % (stats['loads'], stats['attempts'], round(stats['fill_rate'], 3) * 100)
    fillrate_stats.allow_tags = True
    fillrate_stats.short_description = "Fill Rate Stats"

    class Media:
        css = {
            'all': ('customize_tag_admin.css',)
        }
        js = ("customize_tag_admin.js",)

    inlines = [TagTargetInline]
    list_filter = ["publisher", "network", "size", "enabled"]
    list_editable = ['tier', 'value']
    list_display = ['tag_info', 'clickable_publisher', 'clickable_network', 'tier', 'value', "enabled", "floor", "delivery", 'fillrate_stats']
    ordering = ["publisher", 'tier', '-value']
    search_fields = ["tag_name", "publisher__site_name", "network__network_name", "tag"]
    save_as = True
admin.site.register(Tag, TagAdmin)
