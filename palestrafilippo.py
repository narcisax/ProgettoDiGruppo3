class Cliente:  
    def __init__(self, nome, cognome, eta):
        # Inizializza un cliente con nome, cognome ed età
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.registrato = False  # Indica se il cliente è registrato
        self.corsi = []  # Lista dei corsi a cui il cliente è iscritto

class Palestra:
    def __init__(self):
        # Dizionario dei corsi disponibili con i posti rimanenti
        self.corsi = {"Aqua-Gym": 10, 
                      "Preparazione Gare": 10, 
                      "Bimbi-Time": 10}
        self.id = 0  # Identificatore unico per i clienti
        self.listaClienti = [1]  # Lista per memorizzare i clienti registrati
        
    def iscrizione_palestra(self):
        # Metodo per iscrivere un nuovo cliente alla palestra
        self.id += 1  # Incrementa l'ID per ogni nuovo cliente
        
        # Richiesta dati all'utente
        nome = input("Inserisci qui il tuo nome: ")
        nome2 = []
        cognome = input("Inserisci qui il tuo cognome: ")
        eta = int(input("Inserisci qui la tua età: "))
        password = input("Inserisci la tua password: ")
        
        # Creazione dell'oggetto cliente
        n = Cliente(nome, cognome, eta)
        print(f"Ottimo, sei registrato, il tuo id è {self.id}")
        
        nome2.append(password)  # Memorizza la password (errore: non viene utilizzata correttamente)
        self.listaClienti.append(nome)  # Memorizza solo il nome del cliente (errore: non salva password o ID correttamente)
        
    def loggin(self):
        # Metodo per effettuare il login
        id = int(input("Inserisci il tuo id: "))
        password = input("Inserisci la tua password:")    
        
        # Verifica delle credenziali
        if self.listaClienti[id][0] == password:
            print("Loggin avvenuto con successo")
            return True
        print("Tentativo fallito")
        return False
            
    def prenotazione_corsi(self):
        # Metodo per prenotare un corso
        while True:
            iscrizione = int(input("A quale corso vuoi partecipaere?\nAcqua-Gym(1)\nPreparazione Gare (2)\nBimbi-Time(3)\nVisualizza i posti disponibili di ogni corso(4)\n"))
            
            match iscrizione:
                case 1:
                    if self.corsi["Aqua-Gym"] - 1 >= 0:
                        print("Prenotazione effettuata")
                        self.corsi["Aqua-Gym"] - 1  # Errore: non aggiorna il valore
                    else:
                        print("Impossibile effettuare la prenotazione, posti non disponibili")
                case 2:
                    if self.corsi["Preparazione Gare"] - 1 > 0:
                        print("Prenotazione effettuata")
                        self.corsi["Preparazione Gare"] - 1  # Errore: non aggiorna il valore
                case 3:
                    if self.corsi["Bimbi-Time"] - 1 >= 0:
                        print("Prenotazione effettuata")
                        self.corsi["Bimbi-Time"] - 1  # Errore: non aggiorna il valore
                case 4:
                    cosafare = input(f"{self.corsi}, sei interessato a prenotarne uno? (s/n)").lower()
                    if cosafare != 's':
                        break
                case _:
                    print("Scelta non valida")
            
# Creazione di un cliente e della palestra
cliente = Cliente("filippo", "pluto", 12)
palestra = Palestra()

def menu():
    # Menu principale per interagire con l'utente
    while True:
        whatdo = int(input("Cosa vuoi fare?\nIscriverti alla palestra(1)\nIscriverti ad un corso(2)\n"))
        
        match whatdo:
            case 1:
                Palestra.iscrizione_palestra()  # Errore: chiamata non corretta
            case 2:
                iscritto = Palestra.loggin()  # Errore: chiamata non corretta
                if iscritto:
                    Palestra.prenotazione_corsi()  # Errore: chiamata non corretta
            case _:
                break    

menu()
