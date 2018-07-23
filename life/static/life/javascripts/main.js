window.onload = function() {
  
  $('#play-btn').on('click', function() {
    var name = $('#gameroom-input').val();     
    window.location = 'game?roomid=' + name
  });
  
};