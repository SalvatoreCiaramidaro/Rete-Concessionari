class Veicolo:
    def __init__(self, modello, anno, prezzo):
        self.modello = modello
        self.anno = anno
        self.prezzo = prezzo

class Auto(Veicolo):
    def __init__(self, modello, anno, prezzo, numPorte, cavalli):
        super().__init__(modello, anno, prezzo)
        self.numPorte = numPorte
        self.cavalli = cavalli

class Moto(Veicolo):
    def __init__(self, modello, anno, prezzo, numRuote, numCilindrata):
        super().__init__(modello, anno, prezzo)
        self.numRuote = numRuote
        self.numCilindrata = numCilindrata

class Clienti:
    def __init__(self, nome, indirizzo):
        self.nome = nome
        self.indirizzo = indirizzo

class Venditori:
    def __init__(self, nome, id_venditore):
        self.nome = nome
        self.id_venditore = id_venditore

class Showroom:
    def __init__(self, posizione):
        self.posizione = posizione
        self.veicoli = []
        self.venditori = []


class Vendite:
    def __init__(self, id_vendita, data, veicolo, cliente, salesperson):
        self.id_vendita = id_vendita
        self.data = data
        self.veicolo = veicolo
        self.cliente = cliente
        self.salesperson = salesperson

# Variabili di stato
veicoli_in_vendita = []
clienti = []
showrooms = []
venditori = []
vendite_effettuate = []

def aggiungi_showroom():
    posizione = input("Inserisci la posizione dello showroom: ")
    showroom = Showroom(posizione)
    showrooms.append(showroom)
    print("Showroom aggiunto con successo.")

def aggiungi_venditore():
    nome = input("Inserisci il nome del venditore: ")
    id_venditore = int(input("Inserisci l'ID del venditore: "))
    venditore = Venditori(nome, id_venditore)

    print("Showrooms disponibili:")
    for i, showroom in enumerate(showrooms, 1):
        print(f"{i}. {showroom.posizione}")

    try:
        showroom_index = int(input("Seleziona lo showroom a cui associare il venditore (inserisci il numero): ")) - 1
        showrooms[showroom_index].venditori.append(venditore)
        print("Venditore aggiunto con successo allo showroom.")
    except IndexError:
        print("Lo showroom selezionato non esiste.")


def aggiungi_veicolo():
    modello = input("Inserisci il modello del veicolo: ")
    anno = int(input("Inserisci l'anno del veicolo: "))
    prezzo = float(input("Inserisci il prezzo del veicolo: "))
    tipo_veicolo = input("Seleziona il tipo di veicolo (Auto/Moto): ").lower()
    if tipo_veicolo == "auto":
        numPorte = int(input("Inserisci il numero di porte dell'auto: "))
        cavalli = int(input("Inserisci la potenza in cavalli dell'auto: "))
        veicolo = Auto(modello, anno, prezzo, numPorte, cavalli)
    elif tipo_veicolo == "moto":
        numRuote = int(input("Inserisci il numero di ruote della moto: "))
        numCilindrata = int(input("Inserisci la cilindrata della moto: "))
        veicolo = Moto(modello, anno, prezzo, numRuote, numCilindrata)
    else:
        print("Tipo di veicolo non valido.")
        return
    
    print("Showrooms disponibili:")
    for i, showroom in enumerate(showrooms):
        print(f"{i + 1}. {showroom.posizione}")

    try:
        showroom_index = int(input("Seleziona lo showroom dove conservare il veicolo (inserisci il numero): ")) - 1
        showrooms[showroom_index].veicoli.append(veicolo)
        print("Veicolo aggiunto con successo allo showroom.")
    except IndexError:
        print("Lo showroom selezionato non esiste.")


def effettua_vendita():
    print("Veicoli disponibili in vendita:")
    for i, veicolo in enumerate(veicoli_in_vendita, 1):
        print(f"{i}. {veicolo.modello}")
    veicolo_index = int(input("Seleziona il veicolo da vendere (inserisci il numero): ")) - 1
    veicolo = veicoli_in_vendita.pop(veicolo_index)
    cliente_nome = input("Inserisci il nome del cliente: ")
    cliente_indirizzo = input("Inserisci l'indirizzo del cliente: ")
    cliente = Clienti(cliente_nome, cliente_indirizzo)
    venditore_index = int(input("Seleziona il venditore (inserisci l'indice): "))
    venditore = venditori[venditore_index]
    id_vendita = len(vendite_effettuate) + 1
    vendita = Vendite(id_vendita, "2024-02-07", veicolo, cliente, venditore)
    vendite_effettuate.append(vendita)
    print("Vendita effettuata con successo.")

def mostra_veicoli_in_vendita():
    print("Showrooms disponibili:")
    for i, showroom in enumerate(showrooms, 1):
        print(f"{i}. {showroom.posizione}")

    try:
        showroom_index = int(input("Seleziona lo showroom di cui vuoi visualizzare i veicoli in vendita (inserisci il numero): ")) - 1
        veicoli_showroom = showrooms[showroom_index].veicoli
        print(f"Veicoli in vendita nello showroom {showrooms[showroom_index].posizione}:")
        for veicolo in veicoli_showroom:
            print(f"Modello: {veicolo.modello}, Anno: {veicolo.anno}, Prezzo: {veicolo.prezzo}")
    except IndexError:
        print("Lo showroom selezionato non esiste.")


def mostra_vendite_effettuate():
    print("Vendite effettuate:")
    for vendita in vendite_effettuate:
        print(f"ID: {vendita.id_vendita}, Data: {vendita.data}, Veicolo: {vendita.veicolo.modello}, Cliente: {vendita.cliente.nome}, Venditore: {vendita.salesperson.nome}")

def mostra_showrooms():
    print("Showroom disponibili:")
    for showroom in showrooms:
        i = 0
        print(f'Posizione {i+1}: {showroom.posizione}')
def main():
    while True:
        print("\nMENU:")
        print("1. Aggiungi Showroom")
        print("2. Aggiungi Venditore")
        print("3. Aggiungi Veicolo")
        print("4. Effettua Vendita")
        print("5. Mostra Veicoli in Vendita")
        print("6. Mostra Vendite Effettuate")
        print("7. Mostra Showroom")
        print("8. Esci")

        scelta = input("Seleziona un'opzione: ")

        match scelta:
            case "1":
                aggiungi_showroom()
            case "2":
                aggiungi_venditore()
            case "3":
                aggiungi_veicolo()
            case "4":
                effettua_vendita()
            case "5":
                mostra_veicoli_in_vendita()
            case "6":
                mostra_vendite_effettuate()
            case "7":
                mostra_showrooms()
            case "8":
                print("Arrivederci!")
                break

            case _:
                print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
