import os
import threading
import sys
from datetime import datetime
import time

# liste des commandes
def h():
    afficher_heure()
def heure():
    afficher_heure()
def afficher_heure():
    global heure
    format_heure = "{:02d}:{:02d}:{:02d}"
    #sys.stdout.write("\r"+format_heure.format(heure[0], heure[1], heure[2]))
    print(format_heure.format(heure[0], heure[1], heure[2]))
def changer_heure(heures, minutes, secondes):
    global heure
    heure = [heures, minutes, secondes]
def changer_alarme(heures, minutes, secondes):
    global alarme
    alarme = [heures, minutes, secondes]
def afficher_alarme():
    global alarme
    format_alarme = "{:02d}:{:02d}:{:02d}"
    print("Alarme définie pour:",format_alarme.format(alarme[0], alarme[1], alarme[2]))
def liste():
    print("Liste des commandes valides:\n- liste()\n- afficher_heure() | heure() | h()\n- changer_heure(HEURES, MINUTES, SECONDES)\n- changer_alarme(HEURES, MINUTES, SECONDES)\n- afficher_alarme()\n- pause()\n- continuer()\n")
def pause():
    global heure_active
    heure_active = False
def continuer():
    global heure_active
    heure_active = True

def verifier_alarme():
    global heure
    global alarme
    global alarme_activee
    if heure[0] == alarme[0] and heure[1] == alarme[1] and heure[2] == alarme[2]:
        alarme_activee = True
    else:
        alarme_activee = False

def actualiser_heure():
    global heure
    heure[2] += 1
    if heure[2] >= 60:
        heure[2] = 0
        heure[1] += 1
    if heure[1] >= 60:
        heure[1] = 0
        heure[0] += 1
    if heure[0] >= 24:
        heure[0] = 0

def thread_heure():
    global heure
    while True:
        if heure_active:
            verifier_alarme()
            if alarme_activee:
                message = message + "Il est l'heure !"
                print()
            time.sleep(1)
            actualiser_heure()

# Variables globales
heure = [datetime.now().hour, datetime.now().minute, datetime.now().second]
heure_active = True
alarme = [-1, -1, -1]
alarme_activee = False

def horloge():
    input_thread = threading.Thread(target=thread_heure, args=())
    input_thread.start()
    global heure
    global alarme_activee
    print("Bienvenue dans l'HORLOGE !\nPour obtenir une liste des commandes disponibles, entrez \"liste()\".")
    while True:
        message = "Entrez une commande\n"
        if heure_active:
            message = "État: ACTIVE.\t" + message
        else:
            message = "État: EN PAUSE.\t" + message
        cmd = input(message)
        cmd_compiled = compile(cmd, "horloge.py", "exec")
        try:
            exec(cmd_compiled)
        except Exception as e:
            print("Commande invalide !")

horloge()