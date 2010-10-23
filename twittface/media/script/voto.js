$(document).ready( function(){
	
	TARGET_LIST = [];
	LAST_TARGET = [];
	
	refresh_target = function(object_user){
		url_image = object_user["image_url"].replace("_normal.",".");

		$("div#banner", $("div.container")).hide();
		$("div#content", $("div.container")).hide();
		$("p", $("div.container")).html(object_user["last_tweet"]);
		$("input[name='candidato']").val(object_user["id_twitter"]);
		$("div#banner", $("div.container")).css("background-image", "url("+url_image+")");  
		$("span.username", $("div.container")).html("<b>"+object_user["name"]+"</b> " + object_user["name"]);
		$("div#banner", $("div.container")).show();
		$("div#content", $("div.container")).show();
		
		//reload last_voted
		
		if(LAST_TARGET.length > 0){
			var html = '<div class="img_voted">';
			html+= '<img src="/media/images/voted.jpg" height="73" width="73"/>';
			html+= '<span>5</span>';
			html+= '</div>';
			$("div.box_voted").prepend(html);
		}
		
		LAST_TARGET[LAST_TARGET.length] = object_user;
	};
	
	$("div.messageBox").bind("bota_e_tira", function(event, args){
		console.log(args)
		alert(args["msg"]);
		return false;
	});
	
	
	$("div#banner", $("div.container")).bind("next_pic", function(event){
		if(TARGET_LIST.length == 0){
			$.getJSON('/search/result.json?palavra=batom', function(data) {
				TARGET_LIST = data["tweets"];
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
		
	});
	
	$("div#banner", $("div.container")).trigger("next_pic");
	
})