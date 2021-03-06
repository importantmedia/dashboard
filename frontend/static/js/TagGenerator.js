var TagGenerator = {
	dimRegexp : /^([0-9]{2,4})x([0-9]{2,4})/,
	deliveryHost : "http://delivery.lifti.us/" // default
};

TagGenerator.generateTag = function() {
  try {
	var pubid = $("#pubid").val();
	if (! pubid ) {
        $("#tag").val("You must select a publisher to continue.");
		return false;
	}
	var size = $("#size").val();
	if (! size ) {
		$("#tag").val("You must select a size to continue.");
		return false;
	}
    var comments = true;
    var placement = $("#placement").val();

	if ($("#delivery_type").val() == "iframe"){
		var t = TagGenerator.generateIframeTag(pubid, size, comments, placement);
		$("#tag").val(t);
	} else if ($("#delivery_type").val() == "adserver"){
		$("#tag").val(TagGenerator.generateAdServerTag(pubid, size, comments, placement));
	} else {
		$("#tag").val(TagGenerator.generateScriptTag(pubid, size, comments, placement));
	}

	return false;
  } catch (e) {
	alert("Tag Generator Error " + e.message);
	return false;
  }
};

TagGenerator.generateIframeTag = function(pubid, size, comments, placement){
	var url = TagGenerator.deliveryHost + "tag_iframe?pubid=" + pubid + '&size=' + size;
    if (placement) {
        url += "placement=" + escape(placement);
    }
	var t = '';
	if (comments){ t += '<!-- Begin Tag -->\n'; }

	var dim = size.match(TagGenerator.dimRegexp);
	if (! dim){
		return false;
	}

	t += '<iframe src="' + url + '" width="' + dim[1] + '" height="' + dim[2] + '"' +
		' noresize="true" scrolling="no" frameborder="0" marginheight="0"' +
		' marginwidth="0" style="border:none" target="_blank"></iframe>';

	if (comments){ t += '\n<!-- End Tag -->\n'; }
	return t;
};

TagGenerator.generateScriptTag = function(pubid, size, comments, placement){
        var t = '';
        if (comments){
                t += '<!-- Begin Liftium set up. \n' +
                     'This only needs to appear once on your page, anywhere above the tag. -->\n';
        }

        t += '<script>LiftiumOptions = {pubid:"' + pubid + '"}<\/script>\n' +
            '<script src="' + TagGenerator.deliveryHost + 'js/Liftium.js"><\/script>\n';

        if (comments){ t += '<!-- End Liftium set up -->\n'; }
        if (comments){ t += '<!-- Display Tag. Put this in the exact place where you want the ad -->\n'; }
        t += '<script>Liftium.callAd("' + size + '")<\/script>';
        return t;
};

TagGenerator.generateAdServerTag = function(pubid, size, comments, placement){
        var url =  TagGenerator.deliveryHost + 'callAd?pubid=' + pubid + '&slot=' + size;
        if (placement) {
            url += "&placement=" + escape(placement);
        }
        var t = '<script src="' + url + '"><\/script>';
        return t;
};

TagGenerator.doPreview = function(){
    return;
	var size = $("size").value;
	var dim = size.match(TagGenerator.dimRegexp);
	if (! dim){
		return false;
	}

	var iframe = document.getElementById("preview_iframe");
	iframe.width=dim[1];
	iframe.height=dim[2];
	iframe.style.display="block";

	var f = document.getElementById("preview_form");
	f.html.value = $("tag").value;
	return f.submit();
};
