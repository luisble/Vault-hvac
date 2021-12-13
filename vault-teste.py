import hvac, os

def init_server():
    client = hvac.Client(url='http://127.0.0.1:8200', token=os.environ['VAULT_TOKEN'])
    print(f"\n\n Is client authenticated: {client.is_authenticated()}")
    return client

def write_secret(client):
    create_response = client.secrets.kv.v2.create_or_update_secret(path='hello', secret=dict(foo="bar"))
    print('\n\n******* create_response *******\n')
    print(create_response)

def read_secret(client):
    read_response = client.secrets.kv.v2.read_secret_version(path='hello')
    print('\n\n******* read_response *******\n')
    print(read_response)

if __name__ == '__main__':
    vault_server = init_server()
    write_secret(vault_server)
    read_secret(vault_server)
    print('\n\n******* end *******\n')