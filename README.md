# Alura Space

Projeto desenvolvido durante a formação **"Django: crie aplicações em Python"** da Alura. O Alura Space é uma aplicação web que exibe informações sobre a diversos fenômenos do espaço como Galáxias, Nebulosas e etc. O objetivo do projeto é aplicar os conhecimentos e boas práticas do framework Django para criar aplicações web.

---

## **Funcionalidades**

- **Página inicial**: Exibe as imagens adicionadas e um texto informativo.
- **Barra de busca**: Permite pesquisar por imagens ou conteúdos específicos.
- **Categoria das imagens**: Mostra um card com a categoria de cada imagem cadastrada e filtra a apresentação das imagens de acordo com a categoria.
- **Cadastro e login**: Foi cirado uma sessão de cadastro de novos usuarios e login para restrigir o acesso as funções da apliação.
- **Adição e Remoção de imagens**: Permite que usuários cadastrados possam adicionar fotos e permite que a mesma imagem seja removida pelo usuário que a adicionou.
- **Autenticação e Autorização**: Gerenciamento de usuários e permissões no Django Admin.
- **CRUD de Fotografias**: Permite adição, edição, remoção e visualização de fotografias no sistema através do Django Admin.
- **Gerenciamento de Grupos**: Controle de permissões por grupos no Django Admin.

---

## **Tecnologias Utilizadas**

- **Django**: Framework web Python para desenvolvimento rápido e seguro.
- **HTML/CSS**: Para a estruturação e estilização das páginas.
- **Templates Django**: Para reutilização de código e organização do projeto.
- **Banco de Dados SQLite**: Utilizado para armazenar imagens e informações dos usuários.

---

## **Estrutura do Projeto**

```
alura-space/
├── galeria/   # aplicação voltada para a exibição da galeria de imagens
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py   # rotas usadas
│   ├── views.py   # lógicas das páginas
├── setup/
│   ├── static/   # arquivos estaticos a serem carregagos
│   │   ├── assets/
│   │   │   ├── favicon/
│   │   │   ├── ícones/
│   │   │   ├── imagens/
│   │   │   ├── logo/
│   │   ├── styles/   # estilização das páginas
│   │   │   ├── style.css
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py   # configuração do projeto
│   ├── urls.py   # organização geral das urls por aplicação
│   ├── wsgi.py
├── static/   # arquivos estaticos para produção
│   │   ├── admin/
│   │   │   ├── css/
│   │   │   ├── img/
│   │   │   ├── js/
│   │   ├── assets/
│   │   │   ├── favicon/
│   │   │   ├── ícones/
│   │   │   ├── imagens/
│   │   │   ├── logo/
│   │   ├── styles/
│   │   │   ├── style.css
├── templates/   # pastas geral dos templates usados no projeto
│   │   ├── galeria/   # galeria de imagens
│   │   │   ├── buscar.html   # página para resultado das buscas
│   │   │   ├── categoria.html   # página para resultado do filtro de categoria
│   │   │   ├── index.html   # página principal
│   │   │   ├── imagem.html   # página para imagem selecionada
│   │   ├── partials/
│   │   │   │   ├── _alertas   # monta as menssagens de aviso nas páginas
│   │   │   │   ├── _categoria   # monta o menu com as categorias nas páginas destinadas
│   │   │   │   ├── _footer.html   # monta o cabeçãlho nas páginas destinadas
│   │   │   │   ├── _menu.html   # monta um menu que está disponive para todas as págias
│   │   ├── usuarios/   # páginas de acesso dos usuários
│   │   │   ├── cadastro.html   # página que realiza o cadastro de novos usuários
│   │   │   ├── login.html   # página que realiza o login de acesso
│   │   │   ├── novas_fotos.html   # página destinada para adição de novas fotos
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
   - Crie um arquivo `.env` na raiz do projeto e adicione a `SECRET_KEY` do Django:
     ```
     SECRET_KEY=sua_chave_secreta_aqui
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
![Página de Login](https://github.com/user-attachments/assets/d338f7b7-18f1-4a80-919f-67a26debab34)

### Página de Cadastro
![Página de Cadastro](https://github.com/user-attachments/assets/fa2f7283-2aa0-4c8c-a905-f8d01d409905)

### Página Inicial
![Página Inicial](https://github.com/user-attachments/assets/36a544c5-f594-4f19-acc0-ba26762ddd62)

### Página de Imagem
![Página de Imagem](https://github.com/user-attachments/assets/749cd224-282a-40c7-bdd1-820f9d396700)
O usuário logado não tem permissao para excluir fotos de outro usuário

![Página de Imagem](https://github.com/user-attachments/assets/2608032e-2674-48e3-b437-4a6be4c7d6a7)
Já selecionando imagem adicionada por ele mesmo o botão de 'Excluir' fica disponível

### Página de Busca
![Página de Busca](https://github.com/user-attachments/assets/7a71e05c-279d-42b0-bba3-7aad1778f722)

### Página de Categoria
![Página de Categoria](https://github.com/user-attachments/assets/d6912ca1-51ea-4138-ba27-6325574b19e5)

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

---

## **Agradecimentos**

Agradeço à Alura pelo curso incrível e à comunidade Django por fornecer uma ferramenta tão poderosa para desenvolvimento web.

---

## **Contato**

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

- **Email**: reulyson@gmail.com
- **GitHub**: [Reulyson Wanzeler](https://github.com/reulyson)

