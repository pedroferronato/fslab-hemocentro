# fslab-hemocentro
Desenvolvimento do sistema de hemocentros de Rondônia, em parceria com o Hemojipa, hemocentro de Ji-Paraná.

## Instalando o projeto para desenvolvimento
* Instale o Python 3.9.2
* Abra o prompt de comando (cmd) como **administrador**
  * Execute os códigos para instalação e verificação do pipenv:
  ```
  pip install pipenv
  pipenv --version
  ```
* Crie seu ambiente virtual e entre nele:
  ```
  pipenv --three
  pipenv shell
  ```
* Em seu terminal de preferência (evitar terminal interno do VSCode ao usar Windows 10, provável erro ocorrerá) execute:
  ```
  pipenv install
  ```

## Extensões do VSCode recomendadas para o desenvolvimento:
  * Jinja 0.0.8 - wholroyd
  * Jinja2 Snippet Kit 2.0.0 - Wyatt Ferguson
  * Material Icon Theme 
  * GitLens

## Receita do bolo para formulários
  * A estrutura básica de um formulário é: ( breadcrumb + cartão ( titulo + formulário ) )
  ```html
  <div class="contentorConteudo">

    <div class="bread noselect"> </div>

    <div class="cartao noselect"> 
      <div class="titulo">
        <h1>Título</h1>
        <div class="formulario"> </div>
      </div>
    </div>

  </div>
  ```
  * Para cada linha, adicione uma div com a classe ".linhaFormulario"
  ```html
  <div class="contentorConteudo">

    <div class="bread noselect"> </div>

    <div class="cartao noselect"> 
      <div class="titulo">
        <h1>Título</h1>
        <div class="formulario"> 
          <div class="linhaFormulario"> </div>
        </div>
      </div>
    </div>

  </div>
  ```
  * Para cada campo (label + input), adicione uma div com a classe ".campo"
  ```html
  <div class="contentorConteudo">

    <div class="bread noselect"> </div>

    <div class="cartao noselect"> 
      <div class="titulo">
        <h1>Título</h1>
        <div class="formulario"> 
          <div class="linhaFormulario"> 
            <div class="campo">
              <label for="txt">Label:</label>
              <input type="text" id="txt" autocomplete="off">
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
  ```
  * Repita quantas vezes forem nescessárias, campos irão buscar equalidade de largura, na última linha adicione a classe ".ultimaLinhaInput"
  ```html
  <div class="contentorConteudo">

    <div class="bread noselect"> </div>

    <div class="cartao noselect"> 
      <div class="titulo">
        <h1>Título</h1>
        <div class="formulario"> 
          <div class="linhaFormulario"> 
            <div class="campo">
              <label for="txt">Label:</label>
              <input type="text" id="txt" autocomplete="off">
            </div>
            .
            .
            .
            <div class="campo">
              <label for="txt">Label:</label>
              <input type="text" id="txt" autocomplete="off">
            </div>
          </div>
          .
          .
          .
          <div class="linhaFormulario ultimaLinhaInput"> 
            <div class="campo">
              <label for="numRegistro">Número de registro:</label>
              <input type="text" id="numRegistro" autocomplete="off">
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
  ```