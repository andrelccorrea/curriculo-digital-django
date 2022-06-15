# Currículo digital

Criado com Django, oferece a possibilidade de alterar de forma dinâmica o conteúdo do site, com download de currículo e formulário de contato.

Utiliza context processor, gerenciamento automático de dependências por meio do pacote `pip-tools`, gerenciamento de variáveis de ambiente com django-environ, entre outros recursos.

Exemplo hospedado na Oracle Cloud: http://andrecorrea.ddns.net/

# Instalação

### Clone o repositório, instale as dependências e crie um arquivo .env na raiz do projeto no sequinte padrão:

```
DEBUG=True
SECRET_KEY="your_secret_key"
ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0
```

### Crie uma secret key executando o comando abaixo após instalar as dependências:

`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

### Após instalar as dependências pela primeira vez, elas poderão ser gerenciadas por meio do pip-tools:

#### Adicione dependências no arquivo `requirements.in` e compile com:

`pip-compile requirements.in`

#### Instale dependências com:

`pip-sync requirements.txt`