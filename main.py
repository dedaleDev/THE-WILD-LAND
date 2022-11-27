import main_menu
import traceback
dev=True
def main():
    if dev:
        main_menu.main_menu()
    else:
        with open("log.txt", "w") as log:
            try:
                main_menu.main_menu()
            except Exception:
                traceback.print_exc(file=log)
main()