$(function() {

	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = cookies[i].trim();
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}


	function makeTimer(end_time) {
		var endTime = new Date(end_time);
		endTime = Date.parse(endTime) / 1000

		var now = new Date()
		now = Date.parse(now) / 1000

		timeLeft = endTime - now;
		if (timeLeft < 0) {
			manageUserSession("GET");
		}

		var days = Math.floor(timeLeft / 86400); 
		var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
		var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
		var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));

		if (minutes < "10") { minutes = "0" + minutes; }
		if (seconds < "10") { seconds = "0" + seconds; }

		return "Time left: " + minutes + " minutes " + seconds + " seconds";
	}

	function slideSeen() {
		let csrftoken = getCookie('csrftoken');
		$.ajax({
			type: 'PUT',
			url: $("#exam-screen").data('url'),
			data: { 'slide': 'seen' },
			beforeSend: function (xhr, settings) {
				$('div.loading').show();
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			},
			success: function(data)
			{
				manageUserSession("GET");
			},
			error: function(xhr, data)
			{
				console.log(data);
			},
			complete: function () {
				$('div.loading').hide();
			}
		});
	}

	function sendAnswer(id, q_id, phase) {
		let csrftoken = getCookie('csrftoken');
		$.ajax({
			type: 'PUT',
			url: $("#exam-screen").data('url'),
			data: {
				'answer': id,
				'question': q_id,
				'phase': $("#question-box").data('phase')
			},
			beforeSend: function (xhr, settings) {
				$('div.loading').show();
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			},
			success: function(data)
			{
				$("#question-box").append(data.content)
				if ('explanation' in data) {
					$("#explanation").removeClass('d-none');
					$("#explanation-text").html(data.explanation);
					$("#next-question").on('click', function () {
						manageUserSession("GET");
					});
				}
			},
			error: function(xhr, data)
			{
				console.log(data);
			},
			complete: function () {
				$('div.loading').hide();
			}
		});
	}

	function manageUserSession(type) {

		let csrftoken = getCookie('csrftoken');
		let rtnData = undefined;
		$.ajax({
			type: type,
			url: $("#exam-screen").data('url'),
			beforeSend: function (xhr, settings) {
				$('div.loading').show();
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			},
			success: function(data)
			{
				$("#exam-screen").html(data.content);

				if (data.state == 'init') {
					$("#start-exam").on('click', function(e) {
						rtnData = manageUserSession("PATCH"); // start exam
					});
				} else if (data.state == 'start') {
					manageUserSession("GET"); // get actual session state
				} else if (data.state == 'question') {
					$("#phase-text").html($("#question-box").data('phase'));
					$("#timer").html(makeTimer(data.session.stop_time));
					setInterval(function() { $("#timer").html(makeTimer(data.session.stop_time)); }, 1000);
					$(".answer-btn").on('click', function(e) {
						sendAnswer($(e.target).data('pk'), $(e.target).data('qpk'))
					});
				} else if (data.state == 'end' || data.state == 'no_time_left') {
					$("#check-results").on('click', function (e) {
						manageUserSession("GET"); // get actual session state
					});
				} else if (data.state == 'score') {
					console.log('fuckne score');
				} else if (data.state == 'slide') {
					$(".next-slide").on('click', function () {
						slideSeen();
					});
				}

				// console.log(data);
			},
			error: function(xhr, data)
			{
				console.log(data);
			},
			complete: function () {
				$('div.loading').hide();
			}
		});
	}

	manageUserSession("GET"); // get user session
});
