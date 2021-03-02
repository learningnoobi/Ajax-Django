<script>
$(document).ready(function(){
  $("form").on('submit',function(e){
      e.preventDefault();
      const lists = $("form").serialize()
      $.ajax({
            type:"POST",
            url:"{% url 'home' %}",
            data:lists,
            dataType:"json",
            success:function(res){
             const instance = JSON.parse(res.instance)
             console.log(instance)
             const fields = instance[0].fields
             const pk = instance[0].pk;
             console.log(pk)
      
             $('#lists').prepend(`
             <div class="card mt-3 card-c" id="${instance[0].pk}" >
                <div class="card-body">
                    <h5>${fields.name} </h5>
                    <p>${fields.hobby}
                        <span class="float-right">
                            <a  id="${instance[0].pk}"  class="btn btn-danger btn_del">X</a>
                        </span>
                    </p>
                </div>
            </div>      
             `)
             $("#form")[0].reset()
      } 
      })
  })

  //delete single
  $(document).on('click','.btn_del',function(e){
      e.preventDefault()
      const id = this.id
      const url = this.href
      $.ajax({
          url:`/delete/${id}`,
          data:{},
      })
      $("#" + id).fadeOut(300)
      console.log("deleted!")
  })

});
</script>