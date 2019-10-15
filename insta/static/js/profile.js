$(document).ready(function() {
  $('#followers').click(function() {
    $('.followers1').css({'visibility':'visible'})

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
  console.log('ready');
  $("#unfollow").submit(function(event) {
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
          $(".data-follows").empty()
          $(".data-follows").append(
            '<button style="margin:0 10px;padding:5px 20px" class="btn btn-primary btn-sm follow" name="button"> <strong>Follow</strong></button>'
          )
          followers = $("#followers strong").text()
          $("#followers strong").text(parseInt(followers) - 1)
        }
      });
    event.preventDefault()
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
          $(".follow-data").empty()
          $(".follow-data").append(
            '<form id="unfollow">' +
            '<button type="submit" id="unfollow_btn" class="edit btn" name="button"> <strong>Unfollow</strong></button>' +
            '</form>'
          )
          let followers = $("#followers strong").text()
          $("#followers strong").text(parseInt(followers) + 1)
        }
      })
  })

});
