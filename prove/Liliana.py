
#Palestra
corsi_disponibili = {
    "Corso Base Bambini": 80,
    "Corso Intermedio Bambini": 90,
    "Corso Avanzato Bambini": 100,
    "Corso Base Adulti": 85,
    "Corso Intermedio Adulti": 95,
    "Corso Avanzato Adulti": 110,
    "Nuoto Libero Assistito": 60,
    "Acquagym": 70,
    "Nuoto Pre-agonistico": 120,
    "Lezioni Private (individuali)": 150
}


class Palestra:
    def __init__(self,nome):
        self.nome=nome
        self.iscrizioni = []
        
        
    def verif_iscrizione(self):
        for iscrizione in self.iscrizioni:
            if iscrizione['nome'] == nome and iscrizione['corso'] == corso_scelto:
                return True 
        return print("Non presente")
        
        

              
    def corso(self,corsi_disponibile,costo, max_iscritti):
        self.nome_corso=corsi_disponibile
        self.costo=costo
        self.max_iscritti=max_iscritti
        
    
    def iscrizione_palestra(self):
        nome = input("Inserisci il tuo nome: ")
        corso_scelto = input("Inserisci il nome esatto del corso scelto: ")
        
        if self.verif_iscrizione():
            print(f"{nome}, sei già iscritto al corso {corso_scelto}.")
        else:
            print(f"{nome}, ti stai iscrivendo al corso {corso_scelto}.")
            self.partecipazione(nome, corso_scelto)  
            self.iscrizioni.append({'nome': nome, 'corso': corso_scelto})
            print(self.iscrizioni)
        
    def partecipazione(self,nome,corso_scelto):
        if corso_scelto not in corsi_disponibili:
            print("Il corso selezionato non esiste.")
            return
        

        


       
palestra=Palestra("Nuoto")
palestra.iscrizione_palestra()

