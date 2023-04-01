import main_menu
import traceback
import cv2
import pygame
dev=True
def main():
    if dev:
        main_menu.main_menu()
    else:
        #video()
        with open("log.txt", "w") as log:
            try:    
                main_menu.main_menu()
            except Exception:
                traceback.print_exc(file=log)


def video():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.music.load("data/audio.mp3")
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
    
main()