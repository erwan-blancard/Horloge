import threading
from datetime import datetime
import time


def formattage_heure(heures, minutes, secondes):
    if format_12:
        if heures >= 12:
            return FORMAT_HEURE.format(heures-12, minutes, secondes) + " PM"
        else:
            return FORMAT_HEURE.format(heures, minutes, secondes) + " AM"
    else:
        return FORMAT_HEURE.format(heures, minutes, secondes)


# liste des commandes
def h():
    afficher_heure()


def afficher_heure():
    # sys.stdout.write("\r"+format_heure.format(heure[0], heure[1], heure[2]))
    print(formattage_heure(heure[0], heure[1], heure[2]))


def changer_heure(heures, minutes, secondes):
    if (0 <= heures <= 23) and (0 <= minutes <= 59) and (0 <= secondes <= 59):
        global heure
        heure = [heures, minutes, secondes]
        print("Heure définie à:", formattage_heure(heure[0], heure[1], heure[2]) + ".")
    else:
        print("L'heure n'a pas été changée, un ou plusieurs paramètres ne sont pas valides.")


def changer_alarme(heures, minutes, secondes):
    if (0 <= heures <= 23) and (0 <= minutes <= 59) and (0 <= secondes <= 59):
        global alarme
        alarme = [heures, minutes, secondes]
        afficher_alarme()
    else:
        print("L'alarme n'a pas été changée, un ou plusieurs paramètres ne sont pas valides.")


def afficher_alarme():
    if alarme[0] != -1 and alarme[1] != -1 and alarme[2] != -1:
        print("Alarme définie pour:", formattage_heure(alarme[0], alarme[1], alarme[2]) + ".")
    else:
        print("L'alarme n'est pas définie.")


def al():
    afficher_alarme()


def liste():
    print("\nListe des commandes valides:\n- liste()\n- afficher_heure() | h()\n- changer_heure(HEURES, MINUTES, SECONDES)\n- afficher_alarme() | al()\n- changer_alarme(HEURES, MINUTES, SECONDES)\n- changer_format()\n- pause()\n- continuer()\n")


def pause():
    global heure_active
    heure_active = False


def continuer():
    global heure_active
    heure_active = True


def changer_format():
    global format_12
    if format_12:
        format_12 = False
    else:
        format_12 = True
# fin commandes


def verifier_alarme():
    if heure[0] == alarme[0] and heure[1] == alarme[1] and heure[2] == alarme[2]:
        return True
    else:
        return False


def actualiser_heure():
    global heure
    heure[2] += 1
    if heure[2] >= 60 or heure[2] < 0:
        heure[2] = 0
        heure[1] += 1
    if heure[1] >= 60 or heure[1] < 0:
        heure[1] = 0
        heure[0] += 1
    if heure[0] >= 24 or heure[0] < 0:
        heure[0] = 0


def thread_heure():
    global heure
    while True:
        if heure_active:
            verifier_alarme()
            if verifier_alarme():
                print("Il est l'heure !")
            time.sleep(1)
            actualiser_heure()


# Variables globales
heure = [datetime.now().hour, datetime.now().minute, datetime.now().second]
format_12 = False
FORMAT_HEURE = "{:02d}:{:02d}:{:02d}"
heure_active = True
alarme = [-1, -1, -1]
commandes_valides = ["liste", "afficher_heure", "h", "changer_heure", "afficher_alarme", "al", "changer_alarme", "changer_format", "pause", "continuer"]


def commande_valide(cmd):
    for commande in commandes_valides:
        if cmd.startswith(commande+"("):
            return True
    return False


def horloge():
    input_thread = threading.Thread(target=thread_heure, args=())
    input_thread.start()
    print("Bienvenue dans l'HORLOGE !\nPour obtenir une liste des commandes disponibles, entrez \"liste()\".")
    while True:
        message = "Entrez une commande\n"

        if format_12:
            message = "Format: 12H.\t" + message
        else:
            message = "Format: 24H.\t" + message
        if heure_active:
            message = "État: ACTIVE.\t" + message
        else:
            message = "État: EN PAUSE.\t" + message
        message = "\n" + message

        cmd = input(message)
        if commande_valide(cmd):
            try:
                cmd_compiled = compile(cmd, "horloge.py", "exec")
                exec(cmd_compiled)
            except Exception as e:
                print("Commande invalide !")
        else:
            print("Commande invalide !")


horloge()
