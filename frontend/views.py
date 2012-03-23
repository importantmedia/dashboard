from django.shortcuts import render_to_response
from django.template import RequestContext
from frontend.models import Publisher, Tag

def tag_generator(request):
    context = {
        "publishers": Publisher.objects.all(),
        "sizes": dict(Tag.SIZE_CHOICES)
    }
    return render_to_response("tools/tag_generator.html", context, RequestContext(request))
