<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
 </head>
<body>
  <h1>Port Scanner</h1>
  <p>Este é um script em Python que realiza a varredura de portas em um host-alvo. Ele verifica se determinadas portas estão abertas.</p>
  <h2>Uso</h2>
  <ol>
    <li>Clone o repositório ou faça o download do arquivo <code>sps101.py</code>.</li>
    <li>Certifique-se de ter o Python 3 instalado.</li>
    <li>Execute o script no terminal com o comando <code>python sps101.py</code>.</li>
    <li>Insira o alvo (exemplo: exemplo.com), a porta inicial, a porta final e o número de threads.</li>
    <li>Aguarde a conclusão da varredura.</li>
    <li>Verifique a saída para ver quais portas estão abertas.</li>
  </ol>
  <h2>Requisitos</h2>
  <ul>
    <li>Python 3.x</li>
    <li>Módulo <code>socket</code></li>
  </ul>
  <h2>Exemplo</h2>
  <pre><code>$ python sps101.py
Digite o alvo (exemplo: exemplo.com): exemplo.com
Digite a porta inicial: 1
Digite a porta final: 1000
Digite o número de threads: 10

[*] Iniciando varredura de portas em exemplo.com (93.184.216.34)...
[*] Intervalo de portas: 1-1000
[*] Número de threads: 10
[+] Porta 80 aberta
[+] Porta 443 aberta
[*] Varredura de portas concluída.
</code></pre>
  <h2>Contribuição</h2>
  <p>Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, abra um problema ou envie um pull request no <a href="https://github.com/mtzeus/SPS101">repositório do GitHub</a>.</p>
  <h2>Licença</h2>
  <p>Este projeto está licenciado sob a <a href="LICENSE">Licença MIT</a>.</p>
  
</body>
</html>
