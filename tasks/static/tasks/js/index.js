
$(document).on('change', '.tasks', function() {
	var task_id = $(this).val();

	$.ajax({
        url: $(this).data('url'),
        type: 'POST',
        data: {
        	'task_id': task_id,
        	'csrfmiddlewaretoken': csrftoken,
        },
        success: function (data) { },
        failure: function(data) { }
  	});
});

$(document).on('click', '#add_task', function() {
	$('#add_task').remove();
	$('#task_list').append("<div id='new_task'><input type='checkbox' id='new_task_completion'/><input type='text' id='new_task_text'/><button type='button' id='confirm_add'>Add</button><button type='button' id='cancel_add'>X</button></div>"); 
});

$(document).on('click', '#confirm_add', function() {
	var new_task_text = $('#new_task_text').val();
	var new_task_completion = $('#new_task_completion').is(':checked');

	$.ajax({
        url: '/tasks/addTask/',
        type: 'POST',
        data: {
        	'new_task_text': new_task_text,
        	'new_task_completion' : new_task_completion,
        	'csrfmiddlewaretoken': csrftoken,
        },
        success: function (data) { location.reload(); console.log('yes')},
        failure: function(data) { console.log('no') }
  	});
});

$(document).on('click', '#cancel_add', function() {
	$('#new_task').remove();
	$('#add_button_div').append("<button type='button' id='add_task'>Add Task</button>"); 
});