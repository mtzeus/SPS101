Port Scanner
Este é um script simples em Python que realiza uma varredura de portas em um host-alvo. Ele permite que você especifique um intervalo de portas a serem verificadas e o número de threads a serem usadas para a verificação em paralelo.

Uso
Clone o repositório ou faça o download do arquivo sspm.py.

Certifique-se de ter o Python 3 instalado em seu sistema.

Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo sps101.py está localizado.

Execute o script digitando o seguinte comando:

py sps101.py

Siga as instruções fornecidas para inserir as informações necessárias, como o host-alvo (sem o prefixo http:// ou https://), a porta inicial e final a serem verificadas e o número de threads a serem usadas.

Requisitos
Python 3.x
O módulo socket

Exemplo:
--------------------------------------------------
  _____ _____   _____ __  ___  __ 
 / ____|  __ \ / ____/_ |/ _ \/_ |
| (___ | |__) | (___  | | | | || |
 \___ \|  ___/ \___ \ | | | | || |
 ____) | |     ____) || | |_| || |
|_____/|_|    |_____/ |_|\___/ |_|v1. by mtz

Digite o alvo (sem http/https): www.exemplo.com
Digite a porta inicial: 1
Digite a porta final: 1000
Digite o número de threads: 10
[*] Iniciando varredura de portas em exemplo.com (xx.xxx.xxx.xx)...
[*] Intervalo de portas: 1-1000
[*] Número de threads: 10
[+] Porta 80 aberta
[+] Porta 443 aberta
[*] Varredura de portas concluída.
=--------------------------------------------------

Contribuição
Contribuições para este projeto são bem-vindas. Se encontrar algum problema ou quiser sugerir melhorias, sinta-se à vontade para abrir um problema ou enviar uma solicitação de pull no repositório do GitHub.

Licença
Este projeto está licenciado sob a Licença MIT.
