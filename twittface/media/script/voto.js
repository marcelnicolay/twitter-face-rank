$(document).ready( function(){
	
	TARGET_LIST = [];
	LAST_TARGET = [];
	PALAVRA_ORD = "";
	
	
	refresh_target = function(object_user){
		url_image = object_user["image_url"].replace("_normal.",".");

		$("p", $("div.container")).html(object_user["last_tweet"]);
		$("input[name='candidato']").val(object_user["id_twitter"]);
		$("div#banner", $("div.container")).css("background-image", "url("+url_image+")");
		$("span.username", $("div.container")).html("<b>"+object_user["name"]+"</b> " + object_user["name"]);
		$("h4", $("div#content", $("div.container"))).html(PALAVRA_ORD);
		$("div.destaque", $("div.container")).show();
		
		
		//reload last_voted
		
		if(LAST_TARGET.length > 0){
			$("div.box_voted").html("");
			for(i=LAST_TARGET.length-1; i>=0 && LAST_TARGET.length-5<i; i--){
				var html = '<div class="img_voted">';
				html+= '<img src="'+LAST_TARGET[i]["image_url"]+'" height="73" width="73"/>';
				html+= '</div>';
				$("div.box_voted").append(html);
			}
		}
		
		LAST_TARGET[LAST_TARGET.length] = object_user;
		return false;
	};
	
	$("div.messageBox").bind("bota_e_tira", function(event, args){
		//alert(args["msg"]);
		return false;
	});
	
	
	$("div#banner", $("div.container")).bind("next_pic", function(event){
		if(TARGET_LIST.length == 0){
			$.getJSON('/search/result.json?palavra=', function(data) {
				TARGET_LIST = data["tweets"];
				PALAVRA_ORD = data["palavra"] ? data["palavra"] : "(_|_)";
				refresh_target(TARGET_LIST.pop());
			});
		}else{
			refresh_target(TARGET_LIST.pop());
		}
	});


	$("a", $("div.ratings-num")).bind("click", function(){
		var nota = $(this).attr("id");
		var eleitor = $("input[name='eleitor']").val();
		var candidato = $("input[name='candidato']").val();
		var url = "/voto?eleitor="+eleitor+"&candidato="+candidato+"&nota="+nota;
		
		if(nota == "0"){
			$("div#banner", $("div.container")).trigger("next_pic");
		}else{
		
			$.ajax({
			  type: 'POST',
			  url: url,
			  data: { "nota": nota, "eleitor": eleitor, "candidato": candidato  },
			  success: function(data){
				  if (data){
					  if(data.result=="success"){
						  $("div#banner", $("div.container")).trigger("next_pic");
					  }
					  $("div.messageBox").trigger("bota_e_tira", {"res":data.result, "msg":data.message});
				  }
			  },
			  dataType: "json"
			});
		}
		
	});
	
	$("div#banner", $("div.container")).trigger("next_pic");
	
})