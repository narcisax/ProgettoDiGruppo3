<h1 align="left">AQUA SCRIPTS GYM 🌐💦 </h1>


## Descrizione
Questo progetto è un sistema di gestione per una palestra sviluppato in Python. Permette di gestire gli iscritti, le prenotazioni delle lezioni e i pagamenti.

## Funzionalità
- Registrazione e gestione degli utenti
- Gestione delle iscrizioni
- Prenotazione e gestione dei corsi
- Generazione di report sulle attività

Il codice implementa un sistema di gestione per una palestra con le seguenti classi e funzionalità principali:

### Classe `Cliente`
Questa classe rappresenta un cliente della palestra con i seguenti attributi:
- `nome`, `cognome`, `eta`: informazioni personali del cliente.
- `password`: stringa per l'autenticazione.
- `id_cliente`: identificatore univoco del cliente.
- `corsi`: lista dei corsi a cui il cliente è iscritto.

### Classe `Palestra`
Questa classe gestisce la logica della palestra e include:
- Un dizionario `corsi` con i corsi disponibili e i posti rimanenti.
- Un identificatore unico `id` per assegnare nuovi clienti.
- Un dizionario `listaClienti` per memorizzare i clienti registrati.

Le principali funzionalità della classe sono:
1. **`iscrizione_palestra()`**: permette di registrare nuovi clienti.
2. **`loggin()`**: consente ai clienti di accedere con ID e password.
3. **`prenotazione_corsi(id_cliente)`**: permette di prenotare corsi se vi sono posti disponibili.

### Funzione `menu()`
Fornisce un'interfaccia testuale per interagire con il sistema, permettendo agli utenti di:
1. Iscriversi alla palestra.
2. Effettuare il login e prenotare un corso.
3. Uscire dal programma.

## Requisiti
Assicurati di avere installato:
- Python 3.10+

## Contributi
Filippo Giorgio Rondò, Simone Verrengia, Liliana Gilca, Isabella Ponticelli
