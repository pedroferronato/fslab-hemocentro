function abrirCategoriaUm(id){
    if(id == "categoriaUmFechada"){
        delClass('categoriaUmAberta','fechado');
        addClass('categoriaUmAberta','aberto');
        delClass('categoriaUmFechada','aberto')
        addClass('categoriaUmFechada','fechado');
    } else if (id == "categoriaUmAberta"){
        delClass('categoriaUmAberta','aberto');
        addClass('categoriaUmAberta','fechado');
        delClass('categoriaUmFechada','fechado')
        addClass('categoriaUmFechada','aberto');
    } else{
        alert('TEM PARADA ERRADA AE');
    }
}

function abrirCategoriaDois(id){
    if(id == "categoriaDoisFechada"){
        delClass('categoriaDoisAberta','fechado');
        addClass('categoriaDoisAberta','aberto');
        delClass('categoriaDoisFechada','aberto');
        addClass('categoriaDoisFechada','fechado');
    } else if (id == "categoriaDoisAberta"){
        delClass('categoriaDoisAberta','aberto');
        addClass('categoriaDoisAberta','fechado');
        delClass('categoriaDoisFechada','fechado');
        addClass('categoriaDoisFechada','aberto');
    } else{
        alert('TEM PARADA ERRADA AE');
    }
}

function abrirCategoriaTres(id){
    if(id == "categoriaTresFechada"){
        delClass('categoriaTresAberta','fechado');
        addClass('categoriaTresAberta','aberto');
        delClass('categoriaTresFechada','aberto');
        addClass('categoriaTresFechada','fechado');
    } else if (id == "categoriaTresAberta"){
        delClass('categoriaTresAberta','aberto');
        addClass('categoriaTresAberta','fechado');
        delClass('categoriaTresFechada','fechado');
        addClass('categoriaTresFechada','aberto');
    } else{
        alert('TEM PARADA ERRADA AE');
    }
}


function addClass(id, classe) {
    var elemento = document.getElementById(id);
    var classes = elemento.className.split(' ');
    var getIndex = classes.indexOf(classe);
  
    if (getIndex === -1) {
      classes.push(classe);
      elemento.className = classes.join(' ');
    }
  }
  
  function delClass(id, classe) {
    var elemento = document.getElementById(id);
    var classes = elemento.className.split(' ');
    var getIndex = classes.indexOf(classe);
  
    if (getIndex > -1) {
      classes.splice(getIndex, 1);
    }
    elemento.className = classes.join(' ');
  }