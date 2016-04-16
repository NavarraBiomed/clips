function calculate_score(){

	var score = 0;

	if ($("#id_age").val() == 3){
		score += 1;
	}

	if ($("#id_asa").val() >= 3 ){
		score += 1;
	}

	if ($("#id_size").val() >= 40 ){
		score += 1;
	}

	if ($("#id_anticoagulants").val() == 5 || $("#id_anticoagulants").val() == 6 ){
		score += 2;
	}

	if($("#id_location").val() >= 4){
		score += 3;
	}

	return score;
}


function update_score(){
	score = calculate_score();
	$("#id_score").val(score);
	if (score >= 4){
		$("#submit_button").prop('disabled', false);
	} else{
		$("#submit_button").prop('disabled', true);
	}
}

$(document).ready(function(){

update_score();

document.body.addEventListener('click', function(){
	var interval = setInterval(function(){
		update_score();
		clearInterval(interval);
	}, 100);
	

}, true); 

$("#id_size").on('change input paste',function(){
	update_score();
});



});