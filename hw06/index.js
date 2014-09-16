$(document).ready(function () {
	// a lot of what I wanted for this didn't get done because
	// I couldn't get the scraper working. Minimal functionality.

	$(window).on('mouseover', function(ids) {
		// when the mouse is over the window
		if ($(ids.target).attr('id') == 'visualizer') {
	    	// or if the class is visualizer describe the graph
	    	var wcag_nontext = "This bar graph compares the departments, on the x-axis, and the number of courses, on the y-axis.";
	    	$('.department_title').text(wcag_nontext);
	    }

		else if ($(ids.target).attr('id') != '') {
			// if the id of the element it's over isn't blank
			// NOTE: only the rects have ids, all others are classes
			var department_id = $(ids.target).attr('id');
			// set a variable to the id of what the mouse is over
	        $('.department_title').text(department_id);
	        // set the class department_title to the id of the element
	    }
	});

})