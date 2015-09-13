jq(function() {
	jq('.genflattrthing').overlay();

	jq('a.flattr_popup_link').live('click', function(event) {
		refreshOverlay(jq('#flattrthingoverlaycontent'), 
			jq(this).attr('href'));
		return false;
	});

	jq('#flattr_popup_form input[type=checkbox]').live('click', function(event) {
		var target = jq(this);
		var wrap = target.parents('#flattrthingoverlay');
		var fieldName = wrap.find('input[name=fieldName]').attr('value');

		jq('#' + fieldName).val(target.attr('value'));
		
		overlay = jq('.genflattrthing').data('overlay');
		overlay.close();
		return false;
	});

	jq('#create_thing').live('click', function(event) {
		var target = jq(this);
		var wrap = target.parents('#flattr_popup_create');
		var title = wrap.find('input[name=thing_title]').val();

		if(title) {
			target.post(url, {thing_title: title}, function(data) {
			});
		}
		return false;
	});

	jq('input[name=thing_title]').live('click', function(event) {
		var title = jq('#title').val();
		var wrap = jq('#flattr_popup_create input[name=thing_title]');
		if(!wrap.val())
			wrap.val(title);
		return false;
	});

	refreshOverlay(jq('#flattrthingoverlaycontent'), 
		jq('#flattrpopuplink').attr('href'));
});

function refreshOverlay(elem, url) {
	elem.load(url, function() {
		var popup = jq(this).find('#flattr_popup');
		jq('#flattrthingoverlaycontent').html(popup)
	});
}
