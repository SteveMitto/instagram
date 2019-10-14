$(document).ready(function() {
  console.log('like js');
  $("ul li .like-u").click(function() {
    var clicked = $(this)
    console.log(clicked);
    var post_id = clicked.find($('.post_id'))
    $.get('like/' + post_id.val() + '',
      function(data) {
        console.log(data);
        if (data.status) {
          clicked.css({'color': 'red'})
          likes = $(".post"+data.img_id+" .likes .like_amount").text()
          console.log(likes);
          $(".post"+data.img_id+" .likes .like_amount").text(parseInt(likes)+1)
        } else {
          clicked.css({'color': 'black'})
          likes = $(".post"+data.img_id+" .likes .like_amount").text()
          $(".post"+data.img_id+" .likes .like_amount").text(parseInt(likes)-1)
          console.log(likes);
        }
      })
  })
})
