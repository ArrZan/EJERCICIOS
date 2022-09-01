import os, time

def gotoxy(x, y):
    print("%c[%d;%df" % (0x1B, y, x), end="")
                              
def cls():
    os.system('cls')


class Menu:
    def __init__(self, col=1, fil=1):
        self.col = col
        self.fil = fil

    def menu(self, opciones, titulo):
        cls()
        self.col = 1
        self.fil = 1
        gotoxy(self.col, self.fil);
        print("*" * 76, titulo, "*" * 76)
        ct = 0

        for opcion in opciones:
            ct += 1
            self.fil += 1
            gotoxy(self.col, self.fil);print("{})".format(ct), opcion)
            if ct == 8:
                self.col = self.reajustar(ct)
            elif ct == 16:
                self.col = self.reajustar(ct)
            elif ct == 24:
                self.col = self.reajustar(ct)

        opc = self.__valid(1, self.fil + 2, "Escoja una Opcion[1...{}]: ".format(len(opciones)))
        
        return opc

    def reajustar(self, ct):
        self.fil = 1
        return (ct * 5)+2

    def __valid(self, col, fil, inf):
        gotoxy(col,fil);print(inf)
        while True:
            gotoxy(28,fil);valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(28,fil);print("No existe tal opción...")
                time.sleep(1)
                gotoxy(28,fil);print(" "*40)
        return int(valor)







