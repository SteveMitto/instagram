$(document).ready(function() {
$(document).ajaxStart(function(){
  $('.background-loader').show()

})
$(document).ajaxStop(function(){
  $(' .background-loader').hide()
})

$()
  $('body').click(function(){
    $('.search-results').slideUp(300)
  })
  var searchInterval = null
  $("#search").keyup(function(){

    $("span.loader").show()
    clearInterval(searchInterval)
    searchInterval = setInterval(function(){

    term = $("#search").val()
    $("span.loader").hide()
    $.ajax({
      method:'GET',
      url:'/search/'+term+'',
      global:false,
      statusCode:{
        404:function(){
          $('.search-results').hide()
        },
      }
      })
      .done(function(data){
        res =data.results
        $('.search-results').empty()
        if (data.notFound ){

            $('.search-results').append(
              '<h6 class="text-center">' +term+' has no account <h6>'
            )
        }else{

        for(i=0;i<res.length;i++){
        $('.search-results').append(
          '<li> <a href=/'+res[i].username+' target="_blank">'+
              '<div class="row">'+
                '<div class="col-md-3">'+
                '<img src='+res[i].image+' width="45px" height="45px" class="circle" >'+
                '</div>'+
                '<div class="col-md-9">'+
                '<h6 style="color:black">'+res[i].username+'</h6>'+
                '<small style="color:gray">'+res[i].name+'</small>'+
                "</div>"+
              "</div>"+
          '</a></li>'
        )
      }
    }
          $('.search-results').slideDown(300)
      })
      clearInterval(searchInterval)
    },500)
  })

  $("ul li .like-u").click(function() {
    var clicked = $(this)
    var post_id = clicked.find($('.post_id'))
    $.get('/like/' + post_id.val() + '',
      function(data) {
        if (data.status) {
          clicked.css({'color': 'red'})
          likes = $(".post"+data.img_id+" .likes .like_amount").text()
          $(".post"+data.img_id+" .likes .like_amount").text(parseInt(likes)+1)
        } else {
          clicked.css({'color': 'black'})
          likes = $(".post"+data.img_id+" .likes .like_amount").text()
          $(".post"+data.img_id+" .likes .like_amount").text(parseInt(likes)-1)
        }
      })
  })

  $(".comment-form").submit(function(event){
    imageId = $(this).find($('.imageId'))
    comment = $(this).find($('.comment'))
    $.ajax({
      method:'GET',
      url:'/comment/',
      data:{
        'comment':comment.val(),
        'imageId':imageId.val()
      }
    })
    .done(function(data){
      $(".post_comments"+data.image_id+"").append(
      '<p> <strong>'+data.user+'</strong> '+data.comment+'<br>'+
          '<small style="color:gray">0 minutes</small>'+
        '</p>'
      )
    })
    comment.val('')
    event.preventDefault()

  })
  $('.upload-btn').click(function(){
    $('.upload').css({'visibility':'visible'})
  })
  $('.upload .close').click(
    function() {
      $('.upload').css({'visibility':'hidden'})
    })
})
