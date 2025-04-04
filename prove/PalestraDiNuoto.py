class Cliente:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.registrato = False
        self.abbonato = False
        self.corsi = []

    def entrata(self):
        if not self.registrato:
            print("Il cliente non è registrato!")
        else:
            print(f"Benvenuto {self.nome} nella PALESTRA DI NUOTO!")

    def aggiungi_corso(self, corso):
        if corso not in self.corsi:
            self.corsi.append(corso)
            print(f"Corso {corso} aggiunto per {self.nome} {self.cognome}.")
        else:
            print(f"{self.nome} {self.cognome} è già iscritto al corso {corso}.")


class PalestraNuoto:
    def __init__(self):
        self.clienti = {}
        self.prossimo_id = 1
        self.corsi_disponibili = ["Preparazione gare", "Corso bambini", "Nuoto libero"]

    def iscrivi_cliente(self):
        nome = input("Nome: ").strip()
        cognome = input("Cognome: ").strip()
        eta = input("Età: ").strip()

        if not eta.isdigit():
            print("Errore: l'età deve essere un numero.")
            return

        eta = int(eta)
        abbonato = input("Il cliente è abbonato? (s/n): ").strip().lower() == "s"

        id_cliente = self.prossimo_id
        self.clienti[id_cliente] = Cliente(nome, cognome, eta)
        self.clienti[id_cliente].registrato = True
        self.clienti[id_cliente].abbonato = abbonato
        self.prossimo_id += 1

        print(f"\nIscrizione completata! ID Cliente: {id_cliente}")
        print(f"Benvenuto/a {nome} {cognome}!")

    def visualizza_abbonati(self):
        abbonati = [cli for cli in self.clienti.values() if getattr(cli, "abbonato", False)]

        if not abbonati:
            print("Nessun cliente abbonato.")
            return

        print("Clienti abbonati:")
        for cli in abbonati:
            print(f"- {cli.nome} {cli.cognome}, Età: {cli.eta}")

    def gestisci_corsi(self):
        print("Corsi disponibili:")
        for corso in self.corsi_disponibili:
            print(f"- {corso}")

        print("\n1. Aggiungi corso\n2. Rimuovi corso\n3. Torna al menu")
        scelta = input("Scelta: ").strip()

        if scelta == "1":
            nuovo = input("Nome nuovo corso: ").strip()
            if nuovo and nuovo not in self.corsi_disponibili:
                self.corsi_disponibili.append(nuovo)
                print(f"Corso {nuovo} aggiunto!")
            else:
                print("Corso già esistente o nome non valido!")
        elif scelta == "2":
            corso = input("Nome corso da rimuovere: ").strip()
            if corso in self.corsi_disponibili:
                self.corsi_disponibili.remove(corso)
                print(f"Corso {corso} rimosso!")
            else:
                print("Corso non trovato!")
        elif scelta == "3":
            return
        else:
            print("Scelta non valida!")

    def aggiungi_corso_a_cliente(self):
        self.visualizza_abbonati()
        id_cliente = input("Inserisci l'ID del cliente a cui vuoi assegnare un corso: ").strip()

        if not id_cliente.isdigit():
            print("Errore: l'ID deve essere un numero.")
            return

        id_cliente = int(id_cliente)

        if id_cliente in self.clienti and getattr(self.clienti[id_cliente], "abbonato", False):
            print("Corsi disponibili:")
            for i, corso in enumerate(self.corsi_disponibili, 1):
                print(f"{i}. {corso}")

            scelta = input("Seleziona il numero del corso: ").strip()

            if scelta.isdigit():
                scelta = int(scelta) - 1
                if 0 <= scelta < len(self.corsi_disponibili):
                    self.clienti[id_cliente].aggiungi_corso(self.corsi_disponibili[scelta])
                else:
                    print("Scelta non valida!")
            else:
                print("Errore: inserire un numero valido.")
        else:
            print("Cliente non trovato o non abbonato!")


palestra = PalestraNuoto()

while True:
    print("\nMenu Principale:")
    print("1. Iscrivi nuovo cliente")
    print("2. Visualizza clienti abbonati")
    print("3. Gestisci corsi")
    print("4. Assegna corso a cliente")
    print("5. Esci")

    scelta = input("Scelta: ").strip()

    if scelta == "1":
        palestra.iscrivi_cliente()
    elif scelta == "2":
        palestra.visualizza_abbonati()
    elif scelta == "3":
        palestra.gestisci_corsi()
    elif scelta == "4": 
        palestra.aggiungi_corso_a_cliente()
    elif scelta == "5":
        print("Grazie per aver usato il gestionale!")
        break
    else:
        print("Scelta non valida!")