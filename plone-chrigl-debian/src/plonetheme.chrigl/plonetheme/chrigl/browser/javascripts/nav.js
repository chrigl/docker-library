jQuery(function($) {
	$(document).ready(function() {
		if ($('#portal-column-two').length == 0) {
			$('#portlettoggle').hide();
		}
	});
	$('#portal-globalnav>li.selected').click(function() {
		if(window.innerWidth <= 900) {
			$('#portal-globalnav>li.plain').toggle();
			return false;
		}
	});

	$('#portlettoggle').click(function() {
		$('#portal-column-two').toggle();
		$('#portlettoggle>a>img').toggleClass('rotated');
		return false;
	});
})
