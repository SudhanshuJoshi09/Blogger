function write_down(response) {
  document.write(response)
}

$(function(){
	$('button').click(function(){
		var user = $('#inputUsername').val();
		var pass = $('#inputPassword').val();
		$.ajax({
			url: '/signUp',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response) {
        console.log(response)
      },
			error: function(error){
				console.log(error);
			}
		});
	});
});

