
    //Troca de imagens
    var foto,btbr,bteua,btfr,btjp,btOld;
    foto=document.querySelector('.boxImg02 img');
    bteua=document.querySelector('#bteua');
    btbr=document.querySelector('#btbr');

    
    var paises=['galeria-3.png','galeria-15.png','galeria-14.png','galeria-8.png' ];
    btPaises= document.querySelectorAll('.boxBt02 .btn');

    btPaises.forEach(function(obj,index){
        obj.onclick=function(){
       btPaises[btOld].style.backgroundColor='#333333';
       btPaises[btOld].style.color='#ccc';
          foto.src='img/'+paises[index];
          btOld=index;
          btPaises[index].style.backgroundColor='#eef40c';
        }
    });
    //Exibir uma das fotos sorteada ao carregar a página
    var sorteio=parseInt(Math.random()*paises.length);
    btOld = sorteio;
    foto.src='img/'+paises[sorteio];
   btPaises[sorteio].style.backgroundColor='#eef40c';
   btPaises[sorteio].style.color='#111';

    console.log(sorteio);

    paises.forEach(function(obj,index){
        console.log(obj);
    });