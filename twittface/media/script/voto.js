$(document).ready( function(){


	$("a", $("div.ratings-num")).bind("click", function(){
		
		var nota = $(this).attr("id");
		var eleitor = $("input[name='eleitor']").val();
		var candidato = $("input[name='candidato']").val();
		var url = "/voto?eleitor="+eleitor+"&candidato="+candidato+"&nota="+nota;
		
		$.ajax({
		  type: 'POST',
		  url: url,
		  data: { "nota": nota, "eleitor": eleitor, "candidato": candidato  },
		  success: function(data){
			  alert(data.resultado); 
		  },
		  dataType: "json"
		});

		
	});
	
	
	
	
	
	
})