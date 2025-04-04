class Cliente:  
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.registrato = False
        self.corsi = []

class Palestra:
    def __init__(self):
        self.corsi = {"Aqua-Gym": 10, 
                      "Preparazione Gare": 10, 
                      "Bimbi-Time": 10}
        self.id = 0
        self.listaClienti = [1]
        
    
    def iscrizione_palestra(self):
        self.registrato = False
        
        self.id += 1
        
        nome = input("Inserisci qui il tuo nome: ")
        nome2 = []
        
        cognome = input("Inserisci qui il tuo cognome: ")
        eta = int(input("Inserisci qui la tua età: "))
        password = input("Inserisci la tua password: ")
        n = Cliente(nome, cognome, eta)
        print(f"Ottimo, sei registrato, il tuo id è {self.id}")
        nome2.append(password)
        self.listaClienti.append(nome)
        
    def loggin(self):
        id = int(input("Inserisci il tuo id: "))
        password = input("Inserisci la tua password:")    
        if self.listaClienti[id][0] == password:
            print("Loggin avvenuto con successo")
            return True
        print("Tentativo fallito")
        return False
            
    def prenotazione_corsi(self):
        while True:
            iscrizione = int(input("A quale corso vuoi partecipaere?\nAcqua-Gym(1)\nPreparazione Gare (2)\nBimbi-Time\nVisualizza i posti disponibili di ogni corso(4)\n"))
            match iscrizione:
                case 1:
                    if self.corsi["Aqua-Gym"] - 1 >= 0:
                        print("Prenotazione effettuata")
    
                        self.corsi["Aqua-Gym"] - 1
                    else:
                        print("Impossibile effettuare la prenotazioni, posti non disponibili")
                case 2:
                    if self.corsi["Preparazione Gare"] - 1 >0:
                        print("Prenotazione effettuata")
                        self.corsi["Preparzione Gare"] - 1
                case 3:
                    if self.corsi["Bimbi-Time"] -1 >=0:
                        print("Prenotazione effettuata")
                        self.corsi["Bimbi-Time"] - 1
                case 4:
                    cosafare=input(f"{self.corsi}, sei interessato a prenotarne uno? (s/n)").lower()
                    if cosafare != 's':
                        break
                case _:
                    print("Scelta non valida")
            
              
                    
cliente = Cliente("filippo", "pluto", 12)
palestra = Palestra()
def menu():
    while True:
        whatdo = int(input("Cosa vuoi fare?\nIscriverti alla palestra(1)\nIscriverti ad un corso(2)\n"))
        match whatdo:
            case 1:
                Palestra.iscrizione_palestra()
            case 2:
                iscritto = Palestra.loggin()
                if iscritto:
                    Palestra.prenotazione_corsi()
            case _:
                break    

