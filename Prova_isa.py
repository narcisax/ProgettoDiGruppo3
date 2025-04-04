class Cliente:
    
    def __init__(self, nome, cognome, eta, id_cliente):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.iscritto = False
        self.id_cliente = id_cliente
        self.corsi = []

def entrata(self):
    if self.iscritto == True:
        print("Benvenuto/a nella palesta di nuoto.")
    else:
        print("Devi prima procedere all'iscrizione.")
        
def uscita(self):
    print("Alla prossima lezione!")
    
    
class PalestraDiNuoto:
    def __init__(self): #Dizionario dei corsi disponibili con i posti
        self.corsi = {"Acqua Gym": 15,
                      "Corso di nuoto per adulti": 15,
                      "Corsi di nuoto 0-5 anni": 5,
                      "Corsi di nuoto 6-12 anni": 7}
        self.id_cliente = 0 #id x clienti
        self.listaClienti = {} #dizionario per la lista clienti

def iscrizione_palestra(self):
    if self.iscritto == True:
        print("Sei già registrato!")
    else:
        nome = input("Inserisci il tuo nome: ")
        cognome = input("Inserisci il tuo cognome: ")
        eta = int(input("Inserisci la tua età: "))
        cliente = Cliente(nome, cognome, eta)
        self.id_cliente += 1
        self.iscritto == True
        self.listaClienti[self.id] = cliente
        print(f"Sei registrato, il tuo id è {self.id}")

def prenotazione_corsi(self, id_cliente):
    if id_cliente not in self.listaClienti:
            print("Errore: utente non trovato.")
            return
    while True:
        iscrizione = int(input("A quale corso vuoi partecipare?\nAcqua-Gym(1)\nCorso di nuoto per adulti (2)\nCorsi di nuoto 0-5 anni(3)\nCorsi di nuoto 6-12 anni(4)\nVisualizza i posti disponibili di ogni corso(5)\nEsci(6)\n"))
        match iscrizione:
            case 1:
                if self.corsi["Aqua Gym"] - 1 >= 0:
                    print("Prenotazione effettuata")

                    self.corsi["Aqua Gym"] - 1
                else:
                    print("Impossibile effettuare la prenotazioni, posti non disponibili")
            case 2:
                if self.corsi["Corso di nuoto per adulti"] - 1 >0:
                    print("Prenotazione effettuata")
                    self.corsi["Corso di nuoto per adulti"] - 1
            case 3:
                if self.corsi["Corsi di nuoto 0-5 anni"] -1 >=0:
                    print("Prenotazione effettuata")
                    self.corsi["Corsi di nuoto 0-5 anni"] - 1
            case 4:
                if self.corsi["Corsi di nuoto 6-12 anni"] -1 >=0:
                    print("Prenotazione effettuata")
                    self.corsi["Corsi di nuoto 6-12 anni"] - 1
            case 5:
                    print(f"Posti disponibili per i corsi: {self.corsi}")
                
            case 6:
                    print("Uscita dalla prenotazione corsi.")
                    break
            case _:
                print("Scelta non valida")
# Creazione dell'oggetto Palestra
palestra = PalestraDiNuoto()

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