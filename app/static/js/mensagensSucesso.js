mostraDialogo();

function mostraDialogo(){
    
    if($("#message").is(":visible")){
        return false;
    }

    if(!tempo){
        var tempo = 2000;
    }

    if(!tipo){
        var tipo = "success";
    }

    var cssMessage = "display: block; position: fixed; bottom: 0; left: 20%; right: 20%; width: 60%; padding-bottom: 10px; z-index: 9999";
    var cssInner = "margin: 0 auto; box-shadow: 1px 1px 5px black;";

    var dialogo = "";
    dialogo += '<div id="message" style="'+cssMessage+'">';
    dialogo += '    <div class="alert alert-'+tipo+' alert-dismissable" style="'+cssInner+'">';
    dialogo += '    <a href="#" style="margin-right: 8px" class="close" data-dismiss="alert" aria-label="close">×</a>';
    dialogo +=          'Operação realizada com sucesso';
    dialogo += '    </div>';
    dialogo += '</div>';

    $("body").append(dialogo);
    $("#message").hide();
    $("#message").fadeIn(200);

    setTimeout(function() {
        $('#message').fadeOut(300, function(){
            $(this).remove();
        });
    }, tempo); 

}