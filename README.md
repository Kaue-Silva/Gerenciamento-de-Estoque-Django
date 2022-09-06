# Projeto Gerenciamento de Estoque com Django

## Sobre o Projeto
⚠️ Projeto Em Andamento

Projeto tem como objetivo auxiliar no controle de estoque, com alguns recursos essenciais.
## Informações Sobre o Projeto
Antes de por a mão no codigo foi feito alguns preparativos, como a criação de um projeto no Trello, para melhor organização das tarefas.
<br/>Trello: https://trello.com/b/jWYjglIp/projeto-estoque

O banco de dados tambem está seguindo um modelo pensado previamente:<br/>
<img src="assets/diagram_db.jpg" alt="Digrama do Banco de Dados" width="600px" length="400px">

## Como Inicilizar Projeto
Projeto conta com o Docker que auxilia na parte de execução com o sistema de container, evitando que erros ocorram, pelo simples motivo de estar rodando em outra maquina, com o auxilio do Docker-Compose podemos ter diversos serviços inicializados facilmente, segue abaixo o passo a passo.

⚠️ Para utilizar o Docker e o Docker-Compose sera necessário fazer a instalação dos mesmos, vou deixar alguns links dos site oficial. 
<br/><br/>Docker: https://docs.docker.com/get-docker/ 
<br/> Docker-Compose: https://docs.docker.com/compose/install/


### Inicilizando Projeto com Docker

```bash
# clonar o repositorio
git clone https://github.com/Kaue-Silva/Gerenciamento-de-Estoque-Django.git

# entrar na pasta
cd Gerenciamento-de-Estoque-Django
```
Após clonar o repositorio precisamos configurar as variaveis de ambiente:
- Na raiz do projeto vamos criar um arquivo ".env"
- Dentro dele será necessário configurar as seguintes variaveis
```
# DB Config
POSTGRES_DB= # Aqui vai o nome do banco
POSTGRES_USER= # Aqui vai o usuario do banco
POSTGRES_PASSWORD= # Aqui vai a senha do banco
POSTGRES_HOST= db # Aqui deixa como estar

# Django Config
SECRET_KEY= # Aqui coloquem uma chave segura
```
- Tudo configurado agora so iniciar
``` bash
# Inicializando Docker-Compose/Projeto
docker-compose up
```

Após isto abra seu navegador e entre em http://localhost:8000/

## Tecnologias Utilzadas
⚠️ Lembrando que este projeto tem foco no Back-End
### Back-End
- Python
- Django
- Postgresql
- Docker
- Docker-Compose

### Front-End
- Html
- Css
- Javascript
- Bootstrap
- Jinja 2

## Autor
Kauê S de Carvalho </br>
Desenvolvedor Python Back-End

Linkedin: https://www.linkedin.com/in/kaue-silva2004/