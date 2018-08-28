function getData(e) {
	keyword = e.target.value;
	if (keyword.length > 2) {
	keyword_slug = keyword.replace(' ', '+');
		$.getJSON( "/search?keyword="+keyword_slug, function(json) {
			$('#answer').val(JSON.stringify(json));
		});
	}
}