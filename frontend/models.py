from django.db import models

class AdFormat(models.Model):
    ad_format_name = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return '%s - %s' % (self.ad_format_name, self.size)

    class Meta:
        db_table = u'ad_formats'

#class AdFormatsPublishers(models.Model):
#    publisher_id = models.IntegerField(null=True, blank=True)
#    ad_format_id = models.IntegerField(null=True, blank=True)
#    class Meta:
#        db_table = u'ad_formats_publishers'

#class BeaconAgg(models.Model):
#    hour = models.DateTimeField(null=True, blank=True)
#    tagid = models.IntegerField(null=True, blank=True)
#    previous_attempts = models.IntegerField(null=True, blank=True)
#    country = models.CharField(max_length=18, blank=True)
#    loads = models.IntegerField(null=True, blank=True)
#    rejects = models.IntegerField(null=True, blank=True)

#    class Meta:
#        db_table = u'beacon_agg'

#class FillsDay(models.Model):
#    tag_id = models.IntegerField(primary_key=True)
#    day = models.DateField(primary_key=True)
#    attempts = models.IntegerField(null=True, blank=True)
#    loads = models.IntegerField(null=True, blank=True)
#    rejects = models.IntegerField(null=True, blank=True)
#    class Meta:
#        db_table = u'fills_day'

#class FillsHour(models.Model):
#    tag_id = models.IntegerField(primary_key=True)
#    hour = models.DateTimeField(primary_key=True)
#    attempts = models.IntegerField(null=True, blank=True)
#    loads = models.IntegerField(null=True, blank=True)
#    rejects = models.IntegerField(null=True, blank=True)
#    class Meta:
#        db_table = u'fills_hour'

#class FillsMinute(models.Model):
#    tag_id = models.IntegerField(primary_key=True)
#    minute = models.DateTimeField(primary_key=True)
#    attempts = models.IntegerField(null=True, blank=True)
#    loads = models.IntegerField(null=True, blank=True)
#    rejects = models.IntegerField(null=True, blank=True)
#    class Meta:
#        db_table = u'fills_minute'

#class JavascriptErrors(models.Model):
#    created_at = models.DateTimeField(auto_now_add=True)
#    publisher_id = models.IntegerField(null=True, blank=True)
#    tag_id = models.IntegerField(null=True, blank=True)
#    error_type = models.CharField(max_length=255, blank=True)
#    language = models.CharField(max_length=255, blank=True)
#    browser = models.CharField(max_length=255, blank=True)
#    ip = models.CharField(max_length=255, blank=True)
#    message = models.CharField(max_length=255, blank=True)
#    url = models.CharField(max_length=255, blank=True)
#    line = models.IntegerField(null=True, blank=True)
#    class Meta:
#        db_table = u'javascript_errors'

class Network(models.Model):
    PAY_TYPES = (
       ("Per Click", "Per Click"),
       ("Per Impression", "Per Impression"),
       ("Affliate", "Affliate")
    )

    network_name = models.CharField(unique=True, max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    pay_type = models.CharField(max_length=255, choices = PAY_TYPES, default = "Per Impression")
    enabled = models.BooleanField(default = True)
    supports_threshold = models.BooleanField(default = True, help_text = "Does this network support a threshold (floor)")
  #  default_always_fill = models.BooleanField(default)
    us_only = models.BooleanField(default = True)
    comments = models.TextField(null=True, blank=True)
    contact_info = models.TextField(null=True, blank=True)
    billing_info = models.TextField(null=True, blank=True)
    brand_safety_level = models.IntegerField(null=True, blank=True)
 #   tag_template = models.TextField(blank=True)
 #   scraping_instructions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    reporting_url = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.network_name

    class Meta:
        db_table = u'networks'

class NetworkTagOption(models.Model):
    network = models.ForeignKey(Network)
    option_name = models.CharField(max_length=255)
    required = models.BooleanField(default=False)

    class Meta:
        db_table = u'network_tag_options'

class Publisher(models.Model):
    site_name = models.CharField(unique=True, max_length=255)
    site_url = models.CharField(max_length=255, null=True, blank=True)
    brand_safety_level = models.IntegerField(null=True, blank=True)
    hoptime = models.IntegerField(null=True, blank=True, default = 1500, help_text="How long in milliseconds, to try the chain. Once it's passed, jump to the always fill")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
#    beacon_throttle = models.FloatField()
#   xdm_iframe_path = models.CharField(max_length=255, blank=True)
#   category = models.CharField(choices=CATEGORY_CHOICES, max_length=255, blank=True)
#    privacy_policy = models.IntegerField(null=True, blank=True)
    site_description = models.TextField(blank=True, null = True)
#    site_keywords = models.CharField(max_length=255, blank=True)
#    accepted_tac = models.DateTimeField(null=True, blank=True)
#
    def __unicode__(self):
        return self.site_name

    class Meta:
        db_table = u'publishers'

#class PublisherNetworkLogin(models.Model):
#    network = models.ForeignKey(Network)
#    publisher = models.ForeignKey(Publisher)
#    username = models.CharField(max_length=255)
#    password = models.CharField(max_length=255)
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
#
#    class Meta:
#        db_table = u'publisher_network_logins'


class Tag(models.Model):
    SIZE_CHOICES = (
        ('300x250', '300x250 MR'),
        ('728x90', '728x90 LB'),
        ('160x600', '160x600 WS'),
    )
    TIER_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )

    tag_name = models.CharField(max_length=255, blank=True)
    publisher = models.ForeignKey(Publisher)
    network = models.ForeignKey(Network)
    size = models.CharField(max_length=255, choices = SIZE_CHOICES)
    tier = models.IntegerField(null=True, choices = TIER_CHOICES, help_text="1 being the highest. Tags are sorted by Tier, then value descending.")
    value = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True, help_text="Estimated CPM for this tag. Tags are sorted by Tier, then value descending.")
    floor = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True, help_text="Some networks support an absolute minimum that they will pay. Used to prevent client side logic from adjusting the 'value' below this point.")
    tag = models.TextField(blank=True, help_text="HTML tag supplied by the network", verbose_name="Code")

    always_fill = models.BooleanField(default = False, help_text="Will this tag fill 100% of the time?")
    frequency_cap = models.IntegerField(null=True, blank=True, help_text="Max # times within 24 hours to display this tag for a user. Resets on the users' clock")
    rejection_time = models.IntegerField(null=True, blank=True, help_text="After a default is issued, wait this many minutes before trying again. Recommend that every network that defaults have this set")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
#    auto_update_ecpm = models.BooleanField(default = False)
    enabled = models.BooleanField(default = True)
    max_daily_impressions = models.IntegerField(null=True, blank=True)
    sample_rate = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True, help_text="Issue this tag x% of the time, disregarding all other targeting criteria. Leave blank for 100%")
    pacing = models.FloatField(null=True, blank=True, help_text="Like 'sample rate', issue this tag x% of the time, *respecting* all of its criteria. Leave blank for 100%", verbose_name="Pacing Rate")

    def __unicode__(self):
        return self.tag_name

    class Meta:
        db_table = u'tags'


class TagOption(models.Model):
    tag = models.ForeignKey(Tag)
    option_name = models.CharField(unique=True, max_length=255, blank=True)
    option_value = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = u'tag_options'

class TagTarget(models.Model):

    NAME_CHOICES = (
        ('browser', 'Browser (ex. MSIE)'),
        ('country', 'Country (geo targeting. ex. us)'),
        ('domain', 'Domain (site targeting)'),
    )
    tag = models.ForeignKey(Tag)
    key_name = models.CharField(max_length=255, blank=True, choices = NAME_CHOICES)
    key_value = models.CharField(max_length=255, blank=True)

    def display_name(self):
        return self.key_name.title()

    class Meta:
        db_table = u'tag_targets'
