import requests

# Referências sobre o uso do requests:
#
# Fazendo requisições:
# https://docs.python-requests.org/en/master/user/quickstart/#make-a-request
# Usando JSON retornado:
# https://docs.python-requests.org/en/master/user/quickstart/#json-response-content


def version_exists(package_name, version):
    # TODO
    # Fazer requisição na API do PyPI para checar se a versão existe
    response = requests.get(f'https://pypi.org/pypi/{package_name}/{version}/json')
    if (response.status_code == 200):
        return True
    return False


def latest_version(package_name):
    # TODO
    # Fazer requisição na API do PyPI para descobrir a última versão
    # de um pacote. Retornar None se o pacote não existir.

    response = requests.get(f'https://pypi.org/pypi/{package_name}/json')

    if(response.status_code == 404):
        return None
    
    data = response.json()
    
    latest = data['info']['version']


    return latest
