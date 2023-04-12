import traceback
import main_menu
import cv2
import pygame
import locale
import aideCSV
import requests
import getpass

dev=False
def main():
    langue = locale.getlocale()
    if langue[0][0:2]=="fr":
        aideCSV.remplacerVal("langue","fr")
    else:
        aideCSV.remplacerVal("langue","en")
    if dev:

        main_menu.main_menu()
    else:
        video()
        with open("log.txt", "w") as log:
            try:
                main_menu.main_menu()
            except Exception:
                error = traceback.format_exc()    
                sendError(error)
        main_menu.main_menu()
def video():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.mixer.init()
    if aideCSV.valCorrespondante("langue")=="fr":
        pygame.mixer.music.load("data/audio.mp3")
    else:
        pygame.mixer.music.load("data/audio_en.mp3")
    pygame.mixer.music.play()
    cap = cv2.VideoCapture('data/intro2.mp4')
    
    cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("frame",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    while(cap.isOpened()):
        clock.tick(25)
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('frame',frame)
            if cv2.waitKey(25) & 0xFF == 27 :
                pygame.mixer.music.stop()
                break
        else:
            break
    
    cap.release()
    cv2.destroyAllWindows()
def sendError(error:str):

    # URL de la Firebase
    firebase_url = "https://wildland-77be4-default-rtdb.europe-west1.firebasedatabase.app"
    username = getpass.getuser()
    data = {}
    data["error"] = error


    # Envoi de la requête POST
    response = requests.post(firebase_url + "/Error.json", json=data)

    # Vérification de la réponse
    if response.status_code == 200:
        print("Données enregistrées avec succès")
    else:
        print("Erreur lors de l'enregistrement des données :", response.text)
main()