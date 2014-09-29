$(document).ready(function () {
	// a lot of what I wanted for this didn't get done because
	// I couldn't get the scraper working. Minimal functionality.
	$(window).on('mouseover', function(ids) {
		// when the mouse is over the window
		if ($(ids.target).attr('id') == 'visualizer') {
			// or if the class is visualizer describe the graph
			var default_description = "These graphs show a comparison in the number of seats taken in computer science courses vs math courses in different semesters.";
			$('.department_stats').text(default_description);
		}
		else if ($(ids.target).attr('id') != '') {
			// if the id of the element it's over isn't blank
			var department_id = $(ids.target).attr('id');
			// set a variable to the id of what the mouse is over
			$('.department_stats').text(department_id);
			// set the class department_title to the department and its size
		}
	});
})