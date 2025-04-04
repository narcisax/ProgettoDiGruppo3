class Cliente:  
    def __init__(self, nome, cognome, eta, password, id_cliente):
        # Inizializza un cliente con nome, cognome, età e password
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.password = password
        self.id = id_cliente
        self.corsi = []  # Lista dei corsi a cui il cliente è iscritto

class Palestra:
    def __init__(self):
        # Dizionario dei corsi disponibili con i posti rimanenti
        self.corsi = {
            "Aqua-Gym": 10, 
            "Preparazione Gare": 10, 
            "Bimbi-Time": 10
        }
        self.id = 0  # Identificatore unico per i clienti
        self.listaClienti = {}  # Dizionario per memorizzare i clienti con ID
    
    def iscrizione_palestra(self):
        # Metodo per iscrivere un nuovo cliente alla palestra
        self.id += 1  # Incrementa l'ID per ogni nuovo cliente
        
        # Richiesta dati all'utente
        nome = input("Inserisci qui il tuo nome: ")
        cognome = input("Inserisci qui il tuo cognome: ")
        eta = int(input("Inserisci qui la tua età: "))
        password = input("Inserisci la tua password: ")
        
        # Creazione dell'oggetto cliente
        cliente = Cliente(nome, cognome, eta, password, self.id)
        self.listaClienti[self.id] = cliente  # Salva il cliente nel dizionario
        
        print(f"Ottimo, sei registrato! Il tuo ID è {self.id}")
    
    def loggin(self):
        # Metodo per effettuare il login
        id_cliente = int(input("Inserisci il tuo ID: "))
        password = input("Inserisci la tua password: ")    

        # Verifica delle credenziali
        if id_cliente in self.listaClienti and self.listaClienti[id_cliente].password == password:
            print("Login avvenuto con successo!")
            return id_cliente
        print("Tentativo fallito")
        return None
    
    def prenotazione_corsi(self, id_cliente):
        # Metodo per prenotare un corso
        if id_cliente not in self.listaClienti:
            print("Errore: utente non trovato.")
            return
        
        while True:
            iscrizione = int(input("A quale corso vuoi partecipare?\n1. Aqua-Gym\n2. Preparazione Gare\n3. Bimbi-Time\n4. Visualizza i posti disponibili\n5. Esci\n"))
            
            match iscrizione:
                case 1:
                    if self.corsi["Aqua-Gym"] > 0:
                        self.corsi["Aqua-Gym"] -= 1
                        self.listaClienti[id_cliente].corsi.append("Aqua-Gym")
                        print("Prenotazione effettuata con successo per Aqua-Gym!")
                    else:
                        print("Posti non disponibili per Aqua-Gym.")
                
                case 2:
                    if self.corsi["Preparazione Gare"] > 0:
                        self.corsi["Preparazione Gare"] -= 1
                        self.listaClienti[id_cliente].corsi.append("Preparazione Gare")
                        print("Prenotazione effettuata con successo per Preparazione Gare!")
                    else:
                        print("Posti non disponibili per Preparazione Gare.")
                
                case 3:
                    if self.corsi["Bimbi-Time"] > 0:
                        self.corsi["Bimbi-Time"] -= 1
                        self.listaClienti[id_cliente].corsi.append("Bimbi-Time")
                        print("Prenotazione effettuata con successo per Bimbi-Time!")
                    else:
                        print("Posti non disponibili per Bimbi-Time.")
                
                case 4:
                    print(f"Posti disponibili per i corsi: {self.corsi}")
                
                case 5:
                    print("Uscita dalla prenotazione corsi.")
                    break
                
                case _:
                    print("Scelta non valida. Riprova.")
                    
# Creazione dell'oggetto Palestra
palestra = Palestra()

def menu():
    # Menu principale per interagire con l'utente
    while True:
        whatdo = int(input("Cosa vuoi fare?\n1. Iscriverti alla palestra\n2. Iscriverti a un corso\n3. Esci\n"))
        
        match whatdo:
            case 1:
                palestra.iscrizione_palestra()
            
            case 2:
                id_cliente = palestra.loggin()
                if id_cliente:
                    palestra.prenotazione_corsi(id_cliente)
            
            case 3:
                print("Uscita dal programma.")
                break
            
            case _:
                print("Scelta non valida, riprova.")

menu()
