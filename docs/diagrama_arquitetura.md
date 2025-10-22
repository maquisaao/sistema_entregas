sistema-entregas/
│
├─ backend/                     # Backend Django
│   ├─ entregas/                # App principal Django
│   │   ├─ migrations/          # Migrações do Django
│   │   ├─ __init__.py
│   │   ├─ admin.py
│   │   ├─ apps.py
│   │   ├─ models.py            # Modelos: Motoristas, Clientes, Pedidos, Entregas
│   │   ├─ serializers.py       # Para APIs REST (Django REST Framework)
│   │   ├─ urls.py              # URLs do app
│   │   └─ views.py             # Views/Endpoints
│   │
│   ├─ sistema_entregas/        # Config do projeto Django
│   │   ├─ __init__.py
│   │   ├─ asgi.py
│   │   ├─ settings.py
│   │   ├─ urls.py
│   │   └─ wsgi.py
│   │
│   ├─ manage.py
│   └─ requirements.txt         # Dependências (Django, DRF, psycopg2, etc.)
│
├─ frontend/                     # Futuro frontend em React
│   ├─ public/
│   ├─ src/
│   │   ├─ components/
│   │   ├─ pages/
│   │   ├─ App.js
│   │   └─ index.js
│   └─ package.json
│
├─ docs/                         # Documentação
│   └─ diagrama_arquitetura.md
│
├─ tests/                        # Testes unitários e integração
│   └─ backend_tests.py
│
├─ .gitignore
└─ README.md