# Alura Space

Projeto desenvolvido durante a formação **"Django: crie aplicações em Python"** da Alura. O Alura Space é uma aplicação web que exibe informações sobre a diversos fenômenos do espaço como Galáxias, Nebulosas e etc. O objetivo do projeto é aplicar os conhecimentos e boas práticas do framework Django para criar aplicações web.

---

## **Funcionalidades**

- **Página inicial**: Exibe as imagens adicionadas e um texto informativo.
- **Barra de busca**: Permite pesquisar por imagens ou conteúdos específicos.
- **Filtro de imagens**: Mostra botões com a categoria de cada imagem cadastrada e filtra a apresentação das imagens de acordo com a categoria escolhida.
- **Cadastro e login**: Foi cirado uma sessão de cadastro de novos usuarios e login para restrigir o acesso as funções da apliação.
- **CRUD realizado pelos usuários**: Permite que usuários cadastrados possam adicionar fotos e permite que a mesma imagem seja removida ou editada pelo usuário que a adicionou.
- **Autenticação e Autorização**: Gerenciamento de usuários e permissões no Django Admin.
- **CRUD realizado pelos ADMIN**: Permite adição, edição, remoção e visualização de fotografias no sistema através do Django Admin.
- **Gerenciamento de Grupos**: Controle de permissões por grupos no Django Admin.
- **Autenticação Google**: Uso do OAuth 2.0 para realizar login através da autenticação do google.

---

## **Tecnologias Utilizadas**

- **Django**: Framework web Python para desenvolvimento rápido e seguro.
- **HTML/CSS**: Para a estruturação e estilização das páginas.
- **Templates Django**: Para reutilização de código e organização do projeto.
- **Banco de Dados SQLite**: Utilizado para armazenar imagens e informações dos usuários (localmente).
- **AWS**: Utilizado para armazenar arquivos estáticos e de mídia fora da aplicação.

---

## **Estrutura do Projeto**

```
alura-space/
├── apps/
│   ├── galeria/   # aplicação voltada para a exibição da galeria de imagens
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py   # rotas usadas
│   │   ├── views.py   # lógicas das páginas
│   │
│   ├── usuarios/   # aplicação voltada para a exibição das páginas de login e cadastro
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py   # rotas usadas
│   │   ├── views.py   # lógicas das páginas
│   │
├── setup/
│   ├── static/   # arquivos estaticos a serem carregagos
│   │   ├── assets/
│   │   │   ├── favicon/
│   │   │   ├── ícones/
│   │   │   ├── imagens/
│   │   │   ├── logo/
│   │   │
│   │   ├── styles/   # estilização das páginas
│   │   │   ├── style.css
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py   # configuração do projeto
│   ├── urls.py   # organização geral das urls por aplicação
│   ├── wsgi.py
│   │
├── static/   # arquivos estaticos para produção
│   │   ├── admin/
│   │   ├── assets/
│   │   ├── styles/
│   │
├── templates/   # pastas geral dos templates usados no projeto
│   │   ├── galeria/   # galeria de imagens
│   │   │   ├── editar_foto.html
│   │   │   ├── index.html   # página inicial
│   │   │   ├── imagem.html
│   │   │   ├── novas_fotos.html
│   │   │
│   │   ├── partials/ # partes fixas
│   │   │   │   ├── _alertas   # monta as menssagens de aviso nas páginas
│   │   │   │   ├── _footer.html   # monta o cabeçãlho
│   │   │   │   ├── _menu.html   # monta um menu
│   │   │
│   │   ├── shared/ # páginas base compartilhas com as demais do projeto
│   │   │   │   ├── base.html   # estrutura base de página
│   │   │
│   │   ├── usuarios/   # páginas de acesso dos usuários
│   │   │   ├── cadastro.html
│   │   │   ├── login.html
├── .gitignore
├── manage.py
├── README.md
├── requirements.txt
```

---

## **Como Executar o Projeto**

### **Pré-requisitos**
- Python 3.x instalado.
- Pip (gerenciador de pacotes do Python).

### **Passos para Configuração**

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/reulyson/alura-space.git
   cd alura-space
   ```

2. **Criar e ativar o ambiente virtual**:
   - No macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - No Windows:
     ```bash
     python -m venv venv
     venv\Scripts\Activate
     ```

3. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variáveis de ambiente**:
   - Crie um arquivo `.env` na raiz do projeto e adicione a as credenciais de acesso nessárias:
     ```
     # Credenciais Django
      SECRET_KEY = 'chave_djnago'
      
      # Credenciais de autenticação do google
      CLIENT_ID = 'client_id.apps.googleusercontent.com'
      SECRET = 'chave_secreta'
      
      # Credenciais AWS
      AWS_ACCESS_KEY_ID = 'chave_acesso'
      AWS_SECRET_ACCESS_KEY = 'chave_secreta'
      AWS_STORAGE_BUCKET_NAME = 'nome_bucket_aws')
     
     ```
     - As credenciais serão carregadas no settings.py:
     ```python
     ...
     # SECURITY WARNING: keep the secret key used in production secret!
      SECRET_KEY = os.getenv('SECRET_KEY')
     ...
     # AWS Configuração
     AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
     
     AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
     
     AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
     
     AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
     ...
     ```

5. **Aplicar migrações**:
   ```bash
   python manage.py migrate
   ```

6. **Criar um superusuário para acessar o Django Admin**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Executar o servidor**:
   ```bash
   python manage.py runserver
   ```

8. **Acessar a aplicação**:
   Abra o navegador e acesse:
   ```
   http://127.0.0.1:8000/
   ```

9. **Acessar o Django Admin**:
   ```
   http://127.0.0.1:8000/admin
   ```

---

## **Boas Práticas Aplicadas**

- **DRY (Don't Repeat Yourself)**: Reutilização de código com templates e partials.
- **Segurança**: Uso de variáveis de ambiente para proteger informações sensíveis.
- **Modularização**: Criação de apps específicos para funcionalidades distintas.
- **Gerenciamento de Usuários**: Uso do Django Admin para controle de acessos e permissões.
- **Uso de Grupos**: Permissões organizadas por grupos para facilitar o gerenciamento.

---

## 📸 **Capturas de Tela**

### Página de Login
Página de login com a possibilidade de acesso através da autenticação com o Google.
![Página de Login](https://github.com/user-attachments/assets/7a443779-923b-4fc0-a5f8-20945c872d3b)

### Página de Cadastro
![Página de Cadastro](https://github.com/user-attachments/assets/fa2f7283-2aa0-4c8c-a905-f8d01d409905)

### Página Inicial
![Página Inicial](https://github.com/user-attachments/assets/3033c76f-eec9-4cc3-bed0-4022087d30ae)

### Página de Imagem
- O usuário logado não tem permissao para excluir fotos de outro usuário
![Página de Imagem](https://github.com/user-attachments/assets/304b769e-b255-4922-b9dd-4e12d8f0bd28)

- Quando mudamos de usuário o botão de 'Apagar' e 'Editar' fica disponível
![image](https://github.com/user-attachments/assets/49f90c55-fa23-494e-bfb0-2e31f419b101)

### Página de Edição
![Página de Edição](https://github.com/user-attachments/assets/661218b7-c45a-4a08-be53-4e10a7ac6df1)

### Função de Busca
![Página de Busca](https://github.com/user-attachments/assets/ea3bcaf6-1126-411b-899f-91832bd5ae94)

### Função de Filtro
![Página de Categoria](https://github.com/user-attachments/assets/be9cedcb-db41-4aec-9d7d-714e5e99ceb0)

### Django Admin
![Django Admin](https://github.com/user-attachments/assets/064b6b98-5215-4525-ba2b-8607e45b6500)

### Django Admin Pasta Fotografias
![Django Admin](https://github.com/user-attachments/assets/fe593998-06e5-4202-a052-f744b5ebc05c)

### Django Admin Modificar Fotografia
![Django Admin](https://github.com/user-attachments/assets/5396de39-25b7-419f-8722-453957227e00)

### Django Admin Adicionar Fotografia
![Django Admin](https://github.com/user-attachments/assets/1f9a8155-7e89-456b-a9df-bcb7f0238824)

### Django Admin Usuários
![Django Admin Usuários](https://github.com/user-attachments/assets/622d81a3-6494-4b80-be73-d5f27ffe0b10)

---

## **Aprendizados do Curso**

- Configuração de ambientes virtuais com `venv`.
- Criação de projetos e apps no Django.
- Uso de templates e partials para organizar o código HTML.
- Integração de arquivos estáticos (CSS, imagens) no Django.
- Gerenciamento de usuários, permissões e grupos pelo Django Admin.
- Boas práticas de desenvolvimento, como o princípio DRY.
- Criação de buckets e IAM no AWS para gerenciar e armazenar mídias em nuvem.
- Autenticação de usuários com o OAuth 2.0

---

## **Agradecimentos**

Agradeço à Alura pelo curso incrível e à comunidade Django por fornecer uma ferramenta tão poderosa para desenvolvimento web.

---

## **Contato**

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

- **Email**: reulyson@gmail.com
- **GitHub**: [Reulyson Wanzeler](https://github.com/reulyson)

