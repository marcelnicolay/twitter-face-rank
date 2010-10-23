$(document).ready( function(){
	
	TARGET_LIST = [];
	
	refresh_target = function(object_user){
		$("div#banner", $("div.container")).hide();
		$("div#content", $("div.container")).hide();
		
		$("p", $("div.container")).html(object_user["last_tweet"]);
		$("input[name='candidato']").val(object_user["id_twitter"]);
		$("div#banner", $("div.container")).css("background-image",object_user["image_url"]);
		$("span.username", $("div.container")).html("<b>"+object_user["name"]+"</b> " + object_user["name"]);

		$("div#banner", $("div.container")).show();
		$("div#content", $("div.container")).show();
	};
	
	$("div.messageBox").bind("bota_e_tira", function(event, args){
		console.log(args)
		alert(args["msg"]);
		return false;
	});
	
	
	$("div#banner", $("div.container")).bind("next_pic", function(event){
		
		if(TARGET_LIST.length == 0){
			$.getJSON('/search/result.json?palavra=bunda', function(data) {
				TARGET_LIST = data["tweets"];
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