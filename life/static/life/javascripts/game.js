window.onload = function(){
  
  $('#submit-btn').on('click', function() {
    var heartRate = $('#heartRate').val();     
    var miles = $('#miles').val();
    
    $.get('score', {heartRate: heartRate, miles: miles}).done(
      function(data) {
       $('#heartRate').val('');
       $('#miles').val('');
      }
    );
  });
  
};