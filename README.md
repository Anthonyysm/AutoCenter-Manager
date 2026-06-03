<div align="center">
  <h1>🚗 Auto Center</h1>
  <p><strong>Mostruário digital para revenda de veículos</strong></p>
</div>

---

## ✨ Funcionalidades

- **Catálogo de carros** — Listagem com busca por modelo
- **Detalhes do veículo** — Foto, placa, ano, preço e descrição gerada por IA
- **CRUD completo** — Cadastrar, editar e excluir carros
- **Autenticação** — Registro, login e logout
- **Descrição inteligente** — Geração automática de textos de venda com Google Gemini
- **Inventário automático** — Contagem e valor total atualizados via signals
- **Upload de fotos** — Suporte a JPEG, PNG e AVIF
- **Admin Django** — Gerenciamento completo pelo painel administrativo

---

## 🧱 Tecnologias

| Tecnologia | Versão |
|---|---|
| [Python](https://www.python.org/) | 3.13 |
| [Django](https://www.djangoproject.com/) | 5.2 |
| [Google Gemini](https://ai.google.dev/) | google-genai 2.7 |
| [Bulma](https://bulma.io/) | 0.9.4 |
| [Font Awesome](https://fontawesome.com/) | 6.5 |
| [SQLite](https://www.sqlite.org/) | — |
| [Pillow](https://python-pillow.org/) | 11.2 |
| [pillow-avif-plugin](https://pypi.org/project/pillow-avif-plugin/) | 1.5 |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | 1.2 |

---

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/carros.git
cd carros
```

### 2. Crie e ative um virtualenv

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GOOGLE_API_KEY=sua_chave_aqui
DJANGO_SECRET_KEY=seu_secret_key_aqui
```

> **Gere um `DJANGO_SECRET_KEY`** com:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```
>
> **Gere uma `GOOGLE_API_KEY`** em [Google AI Studio](https://aistudio.google.com/apikey)

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Crie um superusuário (opcional, para o admin)

```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000/cars/](http://127.0.0.1:8000/cars/)

---

## 🖼️ Telas

### Página inicial / Listagem de carros

<p align="center">
  <img src="https://github.com/user-attachments/assets/6ccbe505-2f2c-4482-b1af-cfc2941b9a47" alt="Listagem de carros" width="700">
</p>

### Detalhes do carro

<p align="center">
  <img src="https://github.com/user-attachments/assets/deee266c-b837-41e0-9c97-8cd85ba853fb" alt="Detalhes do carro — Uno com escada" width="500">
</p>

---

## 🧪 Funcionalidades em destaque

### 🤖 Descrição por IA

Ao cadastrar um carro sem descrição (`bio`), o sistema automaticamente gera um texto de venda usando o **Google Gemini 2.5 Flash Lite** com informações de modelo, marca e ano.

### 📊 Inventário automático

Sempre que um carro é adicionado ou removido, um registro de inventário é criado com a quantidade total de veículos e o valor total da frota.

### ✅ Validação de formulários

- Valor mínimo do veículo: **R$ 15.000**
- Ano de fabricação mínimo: **1960**
- Placa nos formatos brasileiro (`AAA-0000`) ou Mercosul (`AAA0A00`)
- Foto obrigatória no cadastro

---

## 🗺️ Rotas

| URL | Função |
|---|---|
| `/cars/` | Listagem de carros |
| `/new_car/` | Cadastrar novo carro |
| `/car/<id>/` | Detalhes do carro |
| `/car/<id>/update` | Editar carro |
| `/car/<id>/delete` | Excluir carro |
| `/register/` | Cadastro de usuário |
| `/login/` | Login |
| `/logout/` | Logout |
| `/admin/` | Painel administrativo |
