# Alura Space

Projeto desenvolvido durante a formação **"Django: crie aplicações em Python"** da Alura. O Alura Space é uma aplicação web que exibe informações sobre a diversos fenômenos do espaço como Galáxias, Nebulosas e etc, com funcionalidades como uma barra de busca e uma seção para as imagens mais acessadas.

---

## 🚀 **Funcionalidades**

- **Página inicial**: Exibe as imagens adicionadas e um texto informativo.
- **Barra de busca**: Permite pesquisar por imagens ou conteúdos específicos.
- **Categoria das imagens: Mostra um card com a categoria de cada imagem cadastrada.
- **Autenticação e Autorização**: Gerenciamento de usuários e permissões no Django Admin.
- **CRUD de Fotografias**: Permite adição, edição, remoção e visualização de fotografias no sistema.
- **Gerenciamento de Grupos**: Controle de permissões por grupos no Django Admin.

---

## 🛠️ **Tecnologias Utilizadas**

- **Django**: Framework web Python para desenvolvimento rápido e seguro.
- **HTML/CSS**: Para a estruturação e estilização das páginas.
- **Templates Django**: Para reutilização de código e organização do projeto.
- **Banco de Dados SQLite**: Utilizado para armazenar imagens e informações dos usuários.

---

## 📚 **Estrutura do Projeto**

```
alura-space/
├── galeria/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py 
├── setup/
│   ├── static/
│   │   ├── assets/
│   │   │   ├── favicon/
│   │   │   ├── ícones/
│   │   │   ├── imagens/
│   │   │   ├── logo/
│   │   ├── styles/
│   │   │   ├── style.css
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── static/
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
├── templates/
│   │   ├── galeria/
│   │   │   ├── partials/
│   │   │   │   ├── _footer.html
│   │   │   │   ├── _menu.html
│   │   │   ├── base.html
│   │   │   ├── buscar.html
│   │   │   ├── index.html
│   │   │   ├── imagem.html
├── .gitignore
├── manage.py
├── README.md
├── requirements.txt
```

---

## ⚙️ **Como Executar o Projeto**

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

## 📝 **Boas Práticas Aplicadas**

- **DRY (Don't Repeat Yourself)**: Reutilização de código com templates e partials.
- **Segurança**: Uso de variáveis de ambiente para proteger informações sensíveis.
- **Modularização**: Criação de apps específicos para funcionalidades distintas.
- **Gerenciamento de Usuários**: Uso do Django Admin para controle de acessos e permissões.
- **Uso de Grupos**: Permissões organizadas por grupos para facilitar o gerenciamento.

---

## 📸 **Capturas de Tela**

### Página Inicial
![Página Inicial](https://github.com/user-attachments/assets/395f08ac-f5b9-4419-85cb-0fdc4fca05cb)

### Página de Imagem
![Página de Imagem](https://github.com/user-attachments/assets/fb3a0f53-c982-459f-bbbb-c6f9824c1a6a)

### Página de Busca
![Página de Busca](https://github.com/user-attachments/assets/d44ac599-4b98-4a1d-b6df-30bb6e64fcf1)

### Django Admin Pasta Fotografias
![Django Admin](https://github.com/user-attachments/assets/543f169d-d6b6-4923-82ab-69a2a9d9b430)

### Django Admin Modificar Fotografia
![Django Admin](https://github.com/user-attachments/assets/b9706600-cec8-4169-b646-84425f53d07c)

### Django Admin Adicionar Fotografia
![Django Admin](https://github.com/user-attachments/assets/1f9a8155-7e89-456b-a9df-bcb7f0238824)


---

## 📚 **Aprendizados do Curso**

- Configuração de ambientes virtuais com `venv`.
- Criação de projetos e apps no Django.
- Uso de templates e partials para organizar o código HTML.
- Integração de arquivos estáticos (CSS, imagens) no Django.
- Gerenciamento de usuários, permissões e grupos pelo Django Admin.
- Boas práticas de desenvolvimento, como o princípio DRY.

---

## 🙌 **Agradecimentos**

Agradeço à Alura pelo curso incrível e à comunidade Django por fornecer uma ferramenta tão poderosa para desenvolvimento web.

---

## 💌 **Contato**

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

- **Email**: reulyson@gmail.com
- **GitHub**: [Reulyson Wanzeler](https://github.com/reulyson)

