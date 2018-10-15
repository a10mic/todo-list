function deleteTodoEntry(todo){
  var $todo = $(todo)
  $todo.parent().remove()
  var id = $todo.data('id')
  $.ajax({
    url: 'delete/' + id,
    method: 'DELETE',
    beforeSend: function(xhr){
      xhr.setRequestHeader('X-CSRFToken',csrf_token)
    }
  })

}
