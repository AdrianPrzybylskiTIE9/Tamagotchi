import os, random, time

class Tamagotchi():
    __hunger = 0
    __mood = 1
    __name = False
    __alive = True

    def __init__(self):
        if not self.__name:
            while(True):
                os.system('cls')
                newName = input('   Jakie jest moje imie: ')
                #max 14 znakow zrobic asfas
                if len(newName) <= 14:
                    self.__name = newName
                    break
    
    #Gettery
    def getHunger(self):
        return self.__hunger
    def getMood(self):
        return self.__mood
    def getName(self):
        return self.__name
    def setAliveStatus(self, status):
        self.__alive = status

    #Settery
    def setHunger(self, newHunger):
        self.__hunger = newHunger
    def setMood(self, newMood):
        self.__mood = newMood
    def setName(self, newName):
        self.__name = newName
    def getAliveStatus(self):
        return self.__alive

    def eat(self):
        os.system('cls')
        print('╭─────────────────────────────╮')
        if self.getHunger() > 0:
            if self.getHunger() < 20:
                self.setHunger(0)
            else:
                self.setHunger(self.getHunger()-20)
            print(f'  [{self.getName()}] - Mniam')
        else:
            print(f'  [{self.getName()}] - Jestem Najedzony')
        print('╰─────────────────────────────╯')

        input('   Nacisnij enter by wrócić: ')

    def play(self):
        os.system('cls')
        print('╭─────────────────────────────╮')
        if self.getHunger() < 100:
            self.setHunger(self.getHunger()+2)
            if self.getMood() > 1:
                self.setMood(self.getMood()-1)
            
            print(f'  [{self.getName()}] - 😎')
        else:
            print(f'  [{self.getName()}] - Jestem głodny, nakarm mnie!')
        print('╰─────────────────────────────╯')
        
        input('   Nacisnij enter by wrócić: ')


    def talk(self):
        os.system('cls')
        dialogues = [
            'Dialog nr 1',
            'Dialog nr 2'   
        ]
        print('╭─────────────────────────────╮')
        if self.getMood() < 4:
            print(f'  [{self.getName()}] - {random.choice(dialogues)}')
            self.setMood(self.getMood()+1)
        else:
            print(f'  [{self.getName()}] - Aktualnie jestem na ciebie wsciekly')
        print('╰─────────────────────────────╯')

        input('   Nacisnij enter by wrócić: ')
    
    def info(self):
        os.system('cls')
        if self.getAliveStatus():
            print('        ╔══════════════════════════╗')

            print(f'        ║ Imię - {self.getName()}', end='')
            for i in range(18-len(self.getName())):
                print(' ', end='')
            print('║')
            
            print(f'        ║ Głód - {self.getHunger()}', end='')
            for i in range(18-len(str(self.getHunger()))):
                print(' ', end='')
            print('║')

            moods = [
                'Zbugowany',
                'Szczęśliwy',
                'Zadowolony',
                'Poddenerwowany',
                'Wściekły'
            ]
            print(f'        ║ Chumor - {moods[self.getMood()]}', end='')
            for i in range(16-len(moods[self.getMood()])):
                print(' ', end='')
            print('║')

            print('        ╚══════════════════════════╝')

            input('   Nacisnij enter by wrócić: ')


    def quit(self):
        exit(())

class Game():
    tamagotchi = Tamagotchi()
    actions = [tamagotchi.quit, tamagotchi.talk, tamagotchi.eat, tamagotchi.play, tamagotchi.info]

    def run(self):
        while True:
            os.system('cls')
            print("""
        ╔═══════════════════════╗
        ║ 0 - Wyjdź z gry       ║
        ║ 1 - Porozmawiaj       ║
        ║ 2 - Nakarm            ║
        ║ 3 - Pobaw się         ║
        ║ 4 - Info              ║
        ╚═══════════════════════╝
        """)
            choice = input('   Co robimy: ')
            self.actions[int(choice)]()


if __name__ == '__main__':
    game = Game()
    game.run()