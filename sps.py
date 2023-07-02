import socket
import threading
import argparse
import re

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
    ascii_art = r''' 
   _____ _____   _____ __  ___  __ 
  / ____|  __ \ / ____/_ |/ _ \/_ |
 | (___ | |__) | (___  | | | | || |
  \___ \|  ___/ \___ \ | | | | || |
  ____) | |     ____) || | |_| || |
 |_____/|_|    |_____/ |_|\___/ |_|v1. by mtz
                                                                      
'''
    print(ascii_art)

    # Solicita o alvo e o intervalo de portas ao usuário
    target_host = input("Digite o alvo (sem http/https) www.github.com): ")
    port_range = input("Digite o intervalo de portas (exemplo: 1-1000): ")

    # Verifica se o intervalo de portas foi especificado corretamente
    match = re.match(r"(\d+)-(\d+)", port_range)
    if not match:
        print("[-] Intervalo de portas inválido. Formato esperado: <porta_inicial>-<porta_final>")
        exit()
    start_port = int(match.group(1))
    end_port = int(match.group(2))

    try:
        # Obtém o endereço IP do host fornecido
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("[-] Falha ao obter o endereço IP do host.")
        exit()

    print(f"[*] Iniciando varredura de portas em {target_host} ({target_ip})...")
    print(f"[*] Intervalo de portas: {start_port}-{end_port}")

    # Cria uma lista de threads
    threads = []
    # Divide o intervalo de portas igualmente entre as threads
    num_threads = min(end_port - start_port + 1, 100)  # Limita o número máximo de threads a 100
    ports_per_thread = (end_port - start_port + 1) // num_threads

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
