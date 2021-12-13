# Vault-hvac
Exemplo de Python com Vault utilizando a biblioteca hvac


Para instalação no Windows, utilize o Chocolatey
```
$choco install vault
```

Para instalação no Ubuntu
```
$curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
```

Adicione o repositório oficial HashiCorp Linux
```
$ sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
```

Atualize e Instale
```
$ sudo apt-get update && sudo apt-get install vault
```


Depois inicie o Servidor de Dev
```
vault server -dev
```

exibirá algumas linhas como abaixo:
```
WARNING! dev mode is enabled! In this mode, Vault runs entirely in-memory
and starts unsealed with a single unseal key. The root token is already
authenticated to the CLI, so you can immediately begin using Vault.

You may need to set the following environment variable:

PowerShell:
    $env:VAULT_ADDR="http://127.0.0.1:8200"
cmd.exe:
    set VAULT_ADDR=http://127.0.0.1:8200

The unseal key and root token are displayed below in case you want to
seal/unseal the Vault or re-authenticate.

Unseal Key: BwX3zDQ9UvpT6SSACFCB/FPkf6mRMqOfS3n2grh20og=
Root Token: s.5BCSuCrBHhuYXcu7mMI13TD8

Development mode should NOT be used in production installations!
```

Por segurança guarde a Unseal Key:
```
echo "BwX3zDQ9UvpT6SSACFCB/FPkf6mRMqOfS3n2grh20og=" > unseal.key
```

E o ID do Root Token - Linux: (remova o "s.")
```
export VAULT_DEV_ROOT_TOKEN_ID="5BCSuCrBHhuYXcu7mMI13TD8"
```
ou no Windows Power Shell: (remova o "s.")
```
$env:VAULT_DEV_ROOT_TOKEN_ID='5BCSuCrBHhuYXcu7mMI13TD8'
```

Para certificar se está tudo certo

configure a variável de ambiente no Linux
```
export VAULT_ADDR='http://127.0.0.1:8200'
```

ou no Windows Power Shell:
```
$env:VAULT_ADDR="http://127.0.0.1:8200"
```

ou no Windows Prompt de Comando:
```
set VAULT_ADDR=http://127.0.0.1:8200
```

e veja o status do servidor
```
vault status
```

HVAC é o cliente API do vault que usaremos para interagir com o servidor do vault.
```
pip install hvac
```
No exemplo tem a inicialização do client, exemplo de gravação e leitura da secret

Não esquecer de configurar a variável de ambiente **VAULT_ADDR** e **VAULT_TOKEN** para funcionar 