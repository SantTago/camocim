document.addEventListener("DOMContentLoaded", function() {
    // Verificar se já existe um cookie indicando que o usuário já visitou o site
    var hasVisited = getCookie('visited');
    
    if (!hasVisited) {
      // Se o usuário não visitou o site antes, mostra a tela de carregamento
      var progressBar = document.getElementById('loading-progress');
      var width = 0; // Largura inicial da barra de progresso
      var interval = setInterval(frame, 25); // Define a função frame para ser chamada a cada 10 milissegundos
  
      function frame() {
        if (width >= 100) { // Se a barra de progresso atingir 100%
          clearInterval(interval); // Limpa o intervalo
          // Oculta a tela branca quando o carregamento estiver concluído
          document.getElementById('overlay').style.display = 'none';
          // Define um cookie indicando que o usuário já visitou o site
          setCookie('visited', true, 1); // O cookie irá expirar após 1 dia
        } else {
          width++; // Incrementa a largura da barra de progresso
          progressBar.style.width = width + '%'; // Define a largura da barra de progresso
        }
      }
    } else {
      // Se o usuário já visitou o site antes, oculta a tela de carregamento
      document.getElementById('overlay').style.display = 'none';
    }
  });
  
  // Função para definir um cookie
  function setCookie(name, value, days) {
    var expires = "";
    if (days) {
      var date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
  }
  
  // Função para obter o valor de um cookie
  function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }
  