from torneira.core.dispatcher import url
from controller.canal import CanalController
from controller.usuario import UsuarioController
from controller.video import VideoController
from controller.comentario import ComentarioController

urls = (
    url("/canal/{canal_id}/videos/{pagina}.{extension}", CanalController, action="videos", name="videos_canal"),
    url("/canal/{canal_id}/videos.{extension}", CanalController, action="videos", name="videos_canal"),

    url("/usuario/{usuario_id}/videos/{pagina}.{extension}", UsuarioController, action="videos", name="videos_usuario"),
    url("/usuario/{usuario_id}/videos.{extension}", UsuarioController, action="videos", name="videos_usuario"),
    
    url("/usuario/{usuario_id}/favoritos/{pagina}.{extension}", UsuarioController, action="favoritos", name="usuario_favoritos"),
    url("/usuario/{usuario_id}/favoritos.{extension}", UsuarioController, action="favoritos", name="usuario_favoritos"),
    
    url("/usuario/favorito", UsuarioController, action="favorito", name="usuario_favorito"),
    url("/usuario/login", UsuarioController, action="login", name="videos_usuario"),
    
    url("/usuario/chave", UsuarioController, action="chave", name="chave"),
    
    url("/video/busca.{extension}", VideoController, action="busca", name="busca"),
    
    url("/video/{uuid}/upload", VideoController, action='upload', name="video_upload"),
    url("/video.{extension}", VideoController, name="video_post"),

    url("/video/{videos_id}.{extension}", VideoController, name="video_index"),
    url("/video/{video_id}/comentarios.{extension}", VideoController, action="comentarios", name="video_comentario"),
    url("/video/{video_id}/videosRelacionados.{extension}", VideoController, action="relacionados", name="video_relacionados"),
    
    url("/video/{video_id}/comentario.{extension}", ComentarioController, action="", name="comentario"),
    url("/comentario/{comentario_id}.{extension}", ComentarioController, action="", name="comentario"),
    
)
