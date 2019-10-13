$(document).ready(function(){
  console.log('ready');
$("#unfollow").submit(function(event){
  var you =$('#you').val()
  var me =$('#me').val()
  var form=$("#unfollow")
  $.ajax({
    method:'POST',
    url:'unfollow/',
    data:form.serialize(),
    dataType:'json'
  })
  .done(function(data){
    if (data.unfollowed){
      $(".data-follows").empty()
      $(".data-follows").append(
        '<button style="margin:0 10px;padding:5px 20px" class="btn btn-primary btn-sm follow" name="button"> <strong>Follow</strong></button>'
      )
      followers = $("#followers strong").text()
      $("#followers strong").text(parseInt(followers)-1)
    }
  });
  event.preventDefault()
});
})
