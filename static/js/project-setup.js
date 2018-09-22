var data = [
	{
		"title": "One",
		"link": "http://github.com/one",
		"img": "assets/img/arduino.jpg",
		"desc": "Some random gibberish...",
		"featured": true,
		"tags": ["CP", "Dev"]
	},
	{
		"title": "Two",
		"link": "http://github.com/two",
		"img": "assets/img/arduino.jpg",
		"desc": "Some other random gibberish...",
		"featured": false,
		"tags": ["ML"]
	}
]
function setup() {
	$.each(data, function(key, val) {
		if (val.featured) {
			$("#featuredProjectsCarousel .carousel-indicators").append(
				'<li data-target="#featuredProjectsCarousel" data-slide-to="' + key + '"' + (key === 0 ? ' class="active"' : '' ) + '></li>'
			)
			$("#featuredProjectsCarousel .carousel-inner").append(
				'<div class="carousel-item' + (key === 0 ? ' active' : '') + '">' +
					'<a href="' + val.link + '">' +
						'<img class="d-block img-fluid" src="' + val.img + '" alt="Arduino">' +
						'<div class="carousel-caption animate">' +
							'<div class="animated fadeInDown">' +
	              '<h3 class="h3-responsive">' + val.title + '</h3>' + 
	              '<p>' + val.desc + '</p>' +
	            '</div>' +
						'</div>' +
					'</a>' +
				'</div>'
			)
		}
	})
}