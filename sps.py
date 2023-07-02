import socket
import threading
import re

def get_ip_address(target_host):
    try:
        ip_address = socket.gethostbyname(target_host)
        return ip_address
    except socket.gaierror:
        print("[-] Erro ao obter o endereço IP do alvo.")
        exit()

def scan_port(target_host, target_port):
    try:
        # Cria um socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define um timeout para a conexão
        sock.settimeout(1)
        # Tenta se conectar ao host na porta especificada
        result = sock.connect_ex((target_host, target_port))
        if result == 0:
            print(f"[+] Porta {target_port} aberta")
        sock.close()
    except KeyboardInterrupt:
        print("\n[-] Programa interrompido pelo usuário.")
        exit()
    except socket.error:
        print(f"[-] Falha ao conectar-se a {target_host}:{target_port}")
        exit()

def main():
    # Apresentação em ASCII
    ascii_art = ''' 
   _____ _____   _____ __  ___  __ 
  / ____|  __ \ / ____/_ |/ _ \/_ |
 | (___ | |__) | (___  | | | | || |
  \___ \|  ___/ \___ \ | | | | || |
  ____) | |     ____) || | |_| || |
 |_____/|_|    |_____/ |_|\___/ |_|v1. by mtz
                                                          
    '''
    print(ascii_art)

    # Solicitação de entrada
    target_host = input("Digite o alvo (sem http/https) exemplp: www.github.com): ")
    target_host = re.sub(r"https?://", "", target_host)  # Remove o prefixo "http://" ou "https://"
    target_ip = get_ip_address(target_host)
    start_port = int(input("Digite a porta inicial: "))
    end_port = int(input("Digite a porta final: "))

    # Verifica se a porta final excede o limite de 65535
    if end_port > 65535:
        print("[-] A porta final excede o limite de 65535. Definindo a porta final como 65535.")
        end_port = 65535

    num_threads = int(input("Digite o número de threads: "))

    print(f"[*] Iniciando varredura de portas em {target_host} ({target_ip})...")
    print(f"[*] Intervalo de portas: {start_port}-{end_port}")
    print(f"[*] Número de threads: {num_threads}")

    # Cria uma lista de threads
    threads = []
    # Divide o intervalo de portas igualmente entre as threads
    port_range = end_port - start_port + 1
    ports_per_thread = port_range // num_threads

    # Cria e inicia as threads
    for i in range(num_threads):
        start = start_port + (i * ports_per_thread)
        end = start + ports_per_thread - 1
        if i == num_threads - 1:  # Última thread pode ficar com as portas restantes
            end = end_port
        for port in range(start, end + 1):
            thread = threading.Thread(target=scan_port, args=(target_ip, port))
            thread.start()
            threads.append(thread)

    # Aguarda todas as threads finalizarem
    for thread in threads:
        thread.join()

    print("[*] Varredura de portas concluída.")

if __name__ == '__main__':
    main()
