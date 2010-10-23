$(document).ready( function(){
	
	TARGET_LIST = [];
	
	refresh_target = function(object_user){
		
		alert(object_user);
		
	},
	
	$("div.messageBox").bind("bota_e_tira", function(event, args){
		console.log(args)
		alert(args["msg"]);
		return false;
	});
	
	
	$("div#banner", $("div.container")).bind("next_pic", function(event){
		
		if(TARGET_LIST.length == 0){
			$.getJSON('/random_target', function(data) {
				TARGET_LIST = data;
				refresh_target(TARGET_LIST[0]);
			});
		}else{
			refresh_target(TARGET_LIST[0]);
		}
		
	});


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
			  if (data){
				  if(data.result=="success"){
					  alert("Processo de refresh do candidato")
				  }
				  $("div.messageBox").trigger("bota_e_tira", {"res":data.result, "msg":data.message});
			  }
		  },
		  dataType: "json"
		});
		
	});
	
	$("div#banner", $("div.container")).trigger("next_pic");
	
})