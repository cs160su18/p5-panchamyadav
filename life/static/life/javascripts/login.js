window.onload = function(){
  
  $('#login').on('click', function() {
    var name = $('#username').val();        
    var pass = $('#password').val();     
    if (name !== undefined && name != null) {
      $.get( "authenticate", { type: 'GET', username: name, password: pass})
        .done(function( data ) {
        window.location = 'login'
      });
    }
  });


  $('#signup').on('click', function() {
    var name = $('#username').val();        
    var pass = $('#password').val();     
    if (name !== undefined && name != null) {
      $.get( "authenticate", { type: 'POST', username: name, password: pass})
        .done(function( data ) {
        window.location = 'signup'
      });
    }
  });
};