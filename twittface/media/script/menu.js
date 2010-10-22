$(document).ready( function(){
	
	$("[id|=sub]").hide();
	$("a[id|=opt]").click(function(){
		
		$("[id|=sub]").hide();
		
		$("a[id|=opt]").each(function() {
			$("#" + this.id).removeClass().addClass("inicial");
		})
		
		$("#" + this.id).removeClass().addClass("selecionado");
		$("#sub-" + this.id.replace("opt-", "" )).slideDown("fast");
		return false;
	})
})