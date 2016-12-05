function update_score(){
    console.log("Update score");
    var b1 = $("#id_boston_left").find("option:selected").attr("value");
    var b2 = $("#id_boston_transverse").find("option:selected").attr("value");
    var b3 = $("#id_boston_right").find("option:selected").attr("value");

    b1 = isNaN(parseInt(b1)) ? 0 : parseInt(b1);
    b2 = isNaN(parseInt(b2)) ? 0 : parseInt(b2);
    b3 = isNaN(parseInt(b3)) ? 0 : parseInt(b3);

    var score = b1+b2+b3;

    $("#boston").attr('value',score);

}

$(document).ready(function(){

    update_score();
    
    document.body.addEventListener('click', function(){
        var interval = setInterval(function(){
            update_score();
            clearInterval(interval);
        }, 100);


    }, true);

    $("#id_boston_left, #id_boston_transverse, #id_boston_right").on('change input paste',function(){
        update_score();
    });
});
