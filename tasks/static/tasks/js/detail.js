$(document).on('click', '#delete', function() {
	$.ajax({
        url: $('delete').data('url'),
        type: 'POST',
        data: {
        	'task_id': {{ task.id }},
        	'csrfmiddlewaretoken': csrftoken,
        },
        success: function (data) { window.location.href = '/tasks/';},
        failure: function(data) { }
  	});
});

$(document).on('click', '#edit', function() {
	$('#task_text').remove();
	$('#edit').remove();
	$('#delete').remove();
	$('#task_title_div').append("<div id='task_title'><h1><input type='text' id='edit_task_text' value='{{ task.task_text }}'><button type='button' id='confirm_edit'>!</button><button type='button' id='cancel_edit'>X</button></h1></div>"); 
});

$(document).on('click', '#cancel_edit', function() {
	$('#edit_task_text').remove();
	$('#confirm_edit').remove();
	$('#cancel_edit').remove();
	$('#task_title_div').append("<h1 id='task_text'>{{ task.task_text }}<button type='button' id='edit'>!</button><button type='button' id='delete'>X</button></h1>"); 
});

$(document).on('click', '#confirm_edit', function() {
	var edit_task_text = $('#edit_task_text').val();

	$.ajax({
        url: '/tasks/editTask/',
        type: 'POST',
        data: {
        	'task_id': {{ task.id }},
        	'task_text': edit_task_text,
        	'csrfmiddlewaretoken': csrftoken,
        },
        success: function (data) { location.reload(); },
        failure: function(data) { }
  	});
});

$(document).on('click', '#back_button', function() {
	window.location.href = '/tasks/';
});