// $(()=>{
//     $('form.like').submit((e)=>{
//         e.preventDefault()
//         form = $('form.like')
//         var likeBtn = $('button[name="post-id"]').val().trim();
//         $.ajax({
//             'url':"{% url 'post_like' %}",
//             'type':'POST',
//             'data': {
//                 'post-id': likeBtn
//             },
//             'dataType':'json',
//             'success':function(data){
//                 alert(data['success'])
//             }
//         })
//     })
// })