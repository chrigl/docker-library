(function($) {

	$(document).ready(function() {
		/* insert script tag for flattr's js api */
		var s = document.createElement('script'), t = document.getElementsByTagName('script')[0];
		/* if the page is running in ssl mode, flattr should also do so */
		var proto = 'http';
		if(window.location.href.indexOf('https://') == 0) {
			proto = 'https';
		}
		s.type = 'text/javascript';
		s.async = true;
		s.src = proto + '://api.flattr.com/js/0.6/load.js?mode=auto';
		t.parentNode.insertBefore(s, t);
	});
	
})(jQuery);
