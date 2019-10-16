$(document).ready(function() {
  to_delete=[]
  $('#followers').click(function() {
    $('.followers1').css({'visibility':'visible'})
    if (to_delete != []){
    for(i=0;i<to_delete.length;i++){
      $(".followers1 .people").remove(".person"+to_delete[i]+"")
    }
  }else{
  }
  });
  $('#following').click(function() {
    $('.followers2').css({'visibility':'visible'})

  });
  $('.display-followers .people .funga').click(function(){
    $('.display-followers').css({'visibility':'hidden'})

  })
  $('.settings-btn').click(function(){
    $('.settings').css({'visibility':'visible'})
  })
  $(".unfollow").click(function() {
    var you = $('#you').val()
    var me = $('#me').val()
    var form = $("#unfollow")
    $.ajax({
        method: 'POST',
        url: 'unfollow/',
        data: form.serialize(),
        dataType: 'json',
        data: {
          'csrfmiddlewaretoken': csrftoken,
          'me': $("#me").val(),
          'you': $("#you").val()
        }
      })
      .done(function(data) {
        if (data.unfollowed) {
          $('.unfollow').hide()
          $('.follow').delay(100).show()
          followers = $("#followers strong").text()
          $("#followers strong").text(parseInt(followers) - 1)
          if(to_delete.includes(parseInt(me))){
          }else{
            to_delete.push(parseInt(me))
          }
        }
      });
  });

  $(".follow").click(function() {
    $.ajax({
        method: 'POST',
        url: 'follow/',
        data: {
          'csrfmiddlewaretoken': csrftoken,
          'me': $("#me").val(),
          'you': $("#you").val()
        }
      })
      .done(function(data) {
        if (data.followed) {
          $('.follow').hide()
          $('.unfollow').delay(100).show()
          if(to_delete.includes(parseInt($("#me").val()))){
            to_delete.pop(parseInt(me))
          }
          let followers = $("#followers strong").text()
          $("#followers strong").text(parseInt(followers) + 1)
        }
      })
  })

});
