import os
import argparse
import logging
import socket
import requests

from datetime import datetime
from urllib.parse import urlparse

# Configuração do logger
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Constantes
NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cve/1.0"
DEFAULT_PORT_RANGE = "1-10000"

def scan_ports(host, port_range):
    open_ports = []
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def get_active_hosts(network):
    active_hosts = []
    for host in network:
        response = os.system("ping -c 1 " + host)
        if response == 0:
            active_hosts.append(host)
    return active_hosts

def check_vulnerabilities(service, version):
    vulnerabilities = []
    try:
        response = requests.get(f"{NVD_API_URL}/cve?cpeMatchString={service}:{version}")
        response.raise_for_status()  # Lança uma exceção em caso de erro HTTP
        data = response.json()
        if "result" in data:
            vulnerabilities = data["result"]["CVE_Items"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na consulta de vulnerabilidades: {e}")
    except (KeyError, ValueError) as e:
        logger.error(f"Erro ao processar resposta da API: {e}")
    return vulnerabilities

def generate_report(results):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"report_{timestamp}.txt"
    with open(filename, "w") as file:
        for host, port, vulnerabilities in results:
            file.write(f"Host: {host}, Port: {port}\n")
            for vulnerability in vulnerabilities:
                cve_id = vulnerability["cve"]["CVE_data_meta"]["ID"]
                description = vulnerability["cve"]["description"]["description_data"][0]["value"]
                file.write(f"\tCVE ID: {cve_id}\n")
                file.write(f"\tDescription: {description}\n\n")
            file.write("\n")
    logger.info(f"Relatório gerado: {filename}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Scanner de vulnerabilidades de rede")
    parser.add_argument("target", help="Endereço IP ou URL do alvo")
    parser.add_argument("--verbose", "-v", action="store_true", help="Exibir informações de logging adicionais")
    return parser.parse_args()

def main():
    args = parse_arguments()
    target = args.target
    parsed_url = urlparse(target)
    if parsed_url.netloc:
        target = socket.gethostbyname(parsed_url.netloc)

    port_range = list(range(1, 10001))
    open_ports = scan_ports(target, port_range)
    active_hosts = get_active_hosts([target])

    if not active_hosts:
        logger.warning("Nenhum host ativo encontrado.")
        return

    results = []
    for host in active_hosts:
        for port in open_ports:
            vulnerabilities = check_vulnerabilities(f"tcp/{port}", "")
            results.append((host, port, vulnerabilities))
    
    generate_report(results)

if __name__ == "__main__":
    main()
