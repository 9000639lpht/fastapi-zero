### HTTP - Codigos de resposta

- 1xx: informativo - utilizada para enviar infos para o cliente de que sua requisicao foi recebida e esta sendo processada (so recebe muda nada, a recebi aqui "depois" eu vejo)

- 2xx: sucesso - indica que a requisicao foi bem sucedida (por exemplo, 200 = OK, 201 = Created), indica que tudo foi bem.

- 3xx: redirecionamento - informa que mais acoes sao necessarias para completar a requisicao (por exemplo, 301 Moved permanently, 302 Found).

- 4xx: erro no cliente - Significa que houve, um erro na requisicao pelo lado do cliente significa que quando vemos um erro do tipo da familia iniciando com 4 e porque o cliente fez "caquinha na requisicao". (400 = Bad request, 404 = Not found)

- 5xx: erro no servidor - Indica um erro no servidor ao procesar a requisicao valida do cliente, ou seja e quando o servidor fez caquinha ou quando o servidor envia como resposta uma mensagem que nao conseguimos saber o que fazer com ela. Exemplo: 500 Internal Server Error, 503 Service Unavailable

> OBS: Mais infos sobre os status codes da WEB esta disponivel no IANA.

### Codigos importantes

- 200 OK: a solicitacao foi bem sucedida. O significado depende do metodo HTTP utilizado na solicitacao
- 201 Created: a solicitacao foi bem sucedida e um novo recurso foi criado como resultado.
- 404 Not found: o recurso solicitado nao pode ser encontrado, sendo frequentemente usado quando o recurso e inexistente
- 422 Unprocessable Entity: usado quando a requisicao esta bem-formada, mas nao pode ser seguida devido a erros semanticos. E comum em APIs ao validar dados de entrada.
- 500 Internal Server Error: quando existe um erro na nossa aplicacao (toda vezes que fizer cacaquinha)


> Por padrao o FastAPI retorna sempre o status code 200 OK, mas voce pode passar via parametro nomeado o valor do que voce quer por exemplo:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/', status_code = 201)
read_root():
return {'msg': 'Ola!'}
```

### HTML

O HTML e o teceiro pilar fundamental da web e o HTML, sigla para Hypertext Markup Language. Trate-se da linguagem de marcacao padrao usada para criar e estruturar paginas na internet. Quando acessamos um site, o que vemos em nossos navegadores e o resultado da interpretacao do HTML. Essa linguagem utiliza uma serie de tags - ocmo: <html>, <head>,<body> e etc. Sem elas nos veriamos tudo na web como sendo apenas mensagens JSON e seria bem estranho.

> Por padrao o response_class ou tambem chamado de response_type do FastAPI e um arquivo JSON, porem o FastAPI nos da a possibilidade de passarmos por exemplo ter como padrao de response do FastAPI uma pagina html entao quando um verbo for executado por exemplo o FastAPI devolve uma pagina HMTL.

O FastAPI, tambem trabalha com templates entao e possivel fazer mais coisas com o Jinja e etc.

No escopo do estudo iremos lidar apenas com APIs JSON. Entao e o unico tipo que dados que vamos operar e com dados JSON.


### APIs
APIs (Application Programming Interfaces), que frequentemente utilizam JSON para troca de dados. JSON e um formato leve de troca de dados, facil de ler e escrever para humanos, e simples de interpretar e gerar para maquinas.

Se pudermos fazer uma analogia, uma porta para abrirmos temos uma interface um meio onde interagimos com ela que por exemplo pode ser a macaneta da porta, buraco de chave um mecanismo de trancar a porta e etc. E entao quando falamos de API, estamos englobando todo estes elementos como HTML,JSON,HTTP,URL Cabecalho corpo da mensagem e etc tudo isso faz parte da interface de interecao com uma determinada API.

**Erroneamente, ou melhor dizendo conceitualmente a comunidade de computacao difunde que uma Rest API e uma API que trafega dados JSON, entretanto isso e um erro. Para que seja uma API seja do tipo REST obrigatoriamente ela deve trafegar mensagens HTML. Entao uma API que troca JSON nao e REST ela e apenas um RPC, comunicacao de maquina apenas troca dados.**

### JSON
Quando discutimos APIs ditas "modernas", nos referimos a APIs que priorizam o trafego de dados, deixando de lado a camada de apresentacao, como o HTML que o cliente consegue ler e etc. Porem o JSON e legal pois se trafega menos dados e etc.

O objetivo entao e transmitir dados de forma agnostica para diferentes tipos de clientes. Nesse contexto, o JSON se tornou a midia padrao, gracas a sua leveza e facilidade de leitura tanto por humanos quanto por maquinas, resumindo JSON virou o padrao de quase tudo que troca dados na atualidade.

### Contratos
Como o JSON nao possui uma hierarquia de por exemplo onde o cliente pode comecar a ler ou nao aquele objeto recebido pela mensagem e comum que firmemos contratos entre o cliente e o servidor. Ou seja, o servidor firma um contrato com o cliente delimitando algumas coisas como por exemplo: "Olha vou te enviar ai na mensagem um objeto JSON, que ele vai ter os campos titulo,autor,data" etc e esses dados vao ser sempre do tipo int,string e int e entao sabia uqe voce sempre vai receber isso".

Mais tecnicamente falando quando, estamos lidando com compartilhamento de JSON entre cliente e servidor, e crucial estabelecer um entendimento mutuo sobre a estrutura dos dados que serao trocados. A este entendimento, denominamos de **schema**, o schema atua como um contrato definindo a forma e conteudo dos dados trafegados. (serve para documentar o **"esquema"** que foi combinado entre cliente e servidor).

### Pydantic

Para que possamos garantir estes esquema este contrato sobre a troca de informacoes entre cliente e servidor utilizamos o Pydantic, que traduzindo pode ser algo como pedante algo ou alguem que e muito chato burocratico. A lib Pydantic tem a responsabilidade de documentar os dados que fornecemos pra ele da nossa API atuando como um advogado. Ele fica validando, como que foi trocado a mensagem por exemplo o servidor enviou: "mil novessentos e noventa e dois" ele vai dizer opa nao era esperado o formato int: 1982.

Tecnicamente dentro do universo de APIs e contratos de dados, especialmente ao trabalhar com Python
o Pydantic se destaca como uma ferramenta poderosa e versatil. Alem de embutida ja no FastAPI, a ideia dele e criar uma camada de documentacao, via OpenAPI, e de fazer a validacao dos modelos de entrada e saida da nossa API.