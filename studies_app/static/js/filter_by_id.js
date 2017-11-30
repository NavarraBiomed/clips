$(document).ready(function(){
    searchInput = $("#search-input");
    cases = $(".case");

    $(searchInput).on('input', function(){
        searchID = $(searchInput).val()
        if (searchID==""){
            $(cases).show();
            return;
        }
        $(cases).each(function(){
            id = $(this).attr('data-id');
            if (id.startsWith(searchID)){
                $(this).show()
            } else{
                $(this).hide()
            }
        })
    })

});
