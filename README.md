# ChatPDF

O ChatPDF é uma aplicação Django que permite ao usuário conversar com um chatbot sobre um conteúdo extraído em PDF.

## Configuração do ambiente

1. Certifique-se de ter o Python 3.7 ou superior instalado no seu computador.

2. Clone este repositório para o seu computador:
`bash
Copy code
git clone https://github.com/seu_usuario/chatPDF.git
`

3. Crie um ambiente virtual para o projeto e ative-o:
`bash
Copy code
python3 -m venv myvenv
source myvenv/bin/activate`

4. Instale as dependências do projeto:
`Copy code
pip install -r requirements.txt`

5. Execute as migrações do banco de dados:
`Copy code
python manage.py migrate`

6. Crie um superusuário para acessar a área administrativa:
`Copy codes
python manage.py createsuperuser`

7. Execute o servidor de desenvolvimento:
`Copy code
python manage.py runserver`

8. Acesse a aplicação em http://localhost:8000/.
Estrutura do projeto
- A pasta chatbot contém o aplicativo Django responsável pela funcionalidade do chatbot.
- A pasta exportar contém o aplicativo Django responsável pela funcionalidade de exportar a conversa em formato PDF.
- A pasta core contém as configurações do projeto Django, como as configurações do banco de dados e as configurações do servidor.
- A pasta templates contém os arquivos HTML que são renderizados pela aplicação.
- O arquivo requirements.txt contém as dependências do projeto.

## Contribuindo
Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma solicitação de pull ou uma issue no GitHub.

## sLicença
Este projeto está licenciado sob a Licença MIT.