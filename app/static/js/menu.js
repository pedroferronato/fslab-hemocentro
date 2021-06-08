function abrirMenu() {
    document.getElementById("barraLateral").style.display = "block";
    document.getElementById("barraLateral").style.position = "fixed";
    document.getElementById("barraLateralSombra").style.display = "block";
    document.getElementById("menu").style.display = "none ";
  }
  
function fecharMenu() {
    document.getElementById("barraLateral").style.display = "none";
    document.getElementById("barraLateralSombra").style.display = "none";
    document.getElementById("menu").style.display = "block";
  }

function abrirPerfil() {
    document.getElementById("barraLateralPerfil").style.display = "block";
    document.getElementById("barraLateralPerfilSombra").style.display = "block";
  }

function fecharPerfil(){
    document.getElementById("barraLateralPerfil").style.display = "none";
    document.getElementById("barraLateralPerfilSombra").style.display = "none";
  }