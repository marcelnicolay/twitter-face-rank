function mudaImagem(id, caminhoDaImagem){
	$("#" + id).click(function(){
		$("#produto_imagem > img").first().attr("src", caminhoDaImagem);
		$(this).hover( 
			function (){
				$(this).css("opacity", "1");
			},
			function (){ 
				$(this).css("opacity", "0.9");
			}
		);
	});
}

$(document).ready(function(){
		mudaImagem("preto", "images/produto_foto_grande_1.jpg");
		mudaImagem("azul", "images/produto_foto_grande_2.jpg");
		mudaImagem("cinza", "images/produto_foto_grande_3.jpg");
});