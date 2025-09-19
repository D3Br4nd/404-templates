# CaTE 2026 - Servizio 404

Pagina 404 tematica per la Caccia al Tesoro Evolution 2026 "I Cavalieri di Alabastro".

## Avvio

```bash
docker-compose up -d
```

Il servizio sarà disponibile sulla porta 8080. Configurare nginx proxy manager per puntare a `localhost:8080` e servire su https://cate.prolocoventicano.com

## Struttura

```
app/
├── main.py              # Applicazione Flask
├── templates/404.html   # Template pagina 404
└── static/
    ├── logo-CaTE.png    # Logo evento
    └── favicon.ico      # Favicon
```

Qualsiasi URL richiesto mostrerà la pagina 404 a tema "Cavalieri di Alabastro".
