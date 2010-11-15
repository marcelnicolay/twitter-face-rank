$(document).ready(function() {

	$.ajax({
		type: "GET",
		url: "/campanha/lista",
		dataType: "json",
		success: function(response) {
			inner_html = "";
			
            $.each(response.campanhas, function(index, campanha) {
            	inner_html = inner_html + "<div class='linha-item-proxima-campanha'>";
            	inner_html = inner_html + "<div class='item-proxima-campanha'>" + campanha.nome + "</div>";
            	inner_html = inner_html + "<div class='voto-proxima-campanha'><a href='#' class='votar-campanha' id-campanha='" + campanha.id + "'>[votar]</a></div>";
            	inner_html = inner_html + "</div>";
            });
			
			$('.conteudo-votacao-campanha').html(inner_html);
			
			bind_click_votar();
		},
		error: function() {
			inner_html = '<strong>Ocorreu um erro ao tentar recuperar as campanhas.</strong><br><strong>Tente novamente.</strong>';
			$('.conteudo-votacao-campanha').html(inner_html);
		}
    });

	bind_click_votar = function() {
		$('.votar-campanha').click(function() {
	        $.ajax({
				type: "POST",
				url: "/campanha/voto",
				data: {id: $(this).attr('id-campanha')},
				dataType: "json",
				success: function(response) {
					inner_html = "";
					
	            	inner_html = inner_html + "<div class='agradecemos-seu-voto'>Agradecemos seu voto!</div>";

	            	$.each(response.campanhas, function(index, campanha) {
		            	inner_html = inner_html + "<div class='linha-item-proxima-campanha'>";
		            	inner_html = inner_html + "<div class='item-proxima-campanha'>" + campanha.nome + "</div>";
		            	inner_html = inner_html + "<div class='voto-proxima-campanha'>" + campanha.votos + "</div>";
		            	inner_html = inner_html + "</div>";
		            });
					
					$('.conteudo-votacao-campanha').html(inner_html);
				},
				error: function() {
					alert("Ocorreu um erro ao tentar votar na próxima campanha.\nTente novamente.");
				}
	        });
	
	        return false;
		});
	}
	
});
