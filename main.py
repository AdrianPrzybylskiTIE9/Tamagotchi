import os, random, time, json

# Kolory
blue = "\033[0;34m"
yellow = "\033[0;93m"
green = "\033[0;92m"
resetColour = '\033[0m'

class Tamagotchi():
    __hunger = 0
    __mood = 1
    __name = False
    __alive = True
    loadedState = False

    def __init__(self):
        if not self.__name:
            self.loadGameState()
            if self.loadedState == False:
                while(True):
                    os.system('cls')
                    newName = input(f'[{blue}?{resetColour}] Jakie jest moje imie: ')
                    if len(newName) <= 14:
                        self.setName(newName)
                        break
            self.saveGameState()
    
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

    def loadGameState(self):
        with open('gameData.json', 'r') as f:
            self.gameData = json.load(f)
        
        # print(self.gameData['hunger'])
        try:
            self.setHunger(self.gameData['hunger'])
            self.setMood(self.gameData['mood'])
            self.setName(self.gameData['name'])
            self.loadedState = True
        except:
            self.gameData['hunger'] = self.getHunger()
            self.gameData['mood'] = self.getMood()
            self.gameData['name'] = self.getName()
            self.loadedState = False
    
    def saveGameState(self):
        self.gameData['hunger'] = self.getHunger()
        self.gameData['mood'] = self.getMood()
        self.gameData['name'] = self.getName()
        with open('gameData.json', 'w') as f:
            json.dump(self.gameData, f, indent=2)

    def chatBox(self, prsn, msg):
        print('╭',end='')
        for i in range(len(str(msg))+3+len(prsn)+4):
            print('─',end='')
        print('╮')
        print(f'│ [{green}{prsn}{resetColour}] - {msg} │')
        print('╰',end='')
        for i in range(len(str(msg))+3+len(prsn)+4):
            print('─',end='')
        print('╯')

    def eat(self):
        os.system('cls')
        if self.getHunger() > 0:
            if self.getHunger() < 20:
                self.setHunger(0)
            else:
                self.setHunger(self.getHunger()-20)
            self.chatBox(self.getName(), 'mniam')
        else:
            self.chatBox(self.getName(), 'Jestem Najedzony')

        input(f'[{yellow}!{resetColour}] Nacisnij enter by wrócić: ')

    def play(self):
        os.system('cls')
        if self.getHunger() < 100:
            self.setHunger(self.getHunger()+2)
            if self.getMood() > 1:
                self.setMood(self.getMood()-1)
            
            self.chatBox(self.getName(), 'B)')
        else:
            self.chatBox(self.getName(), 'Jestem głodny, nakarm mnie!')
        
        input(f'[{yellow}!{resetColour}] Nacisnij enter by wrócić: ')


    def talk(self):
        os.system('cls')
        dialogues = [
            'Poopy-di scoop Scoop-diddy-whoop',
            'Jak tam minął dzień?',
            'Miłego dnia :)',
            'Ratio',
            'La, la, la-la (ayy) Wait til I get my money right',
            'Teraz... Albo.. Teraz',
            'Super!',
            'Daleko jeszcze?',
            'Wszystko przed toba!',
            'Jestes najlepszy',
            'Raz sie zyje',
            'YANDHI 9 29 18'
        ]
        if self.getMood() < 4:
            self.chatBox(self.getName(), random.choice(dialogues))
            self.setMood(self.getMood()+1)
        else:
            self.chatBox(self.getName(), 'Aktualnie jestem na ciebie wsciekly')

        input(f'[{yellow}!{resetColour}] - Nacisnij enter by wrócić: ')
    
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

            input(f'[{yellow}!{resetColour}] - Nacisnij enter by wrócić: ')


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
            choice = input(f'[{blue}!{resetColour}] - Co robimy: ')
            self.actions[int(choice)]()
            self.tamagotchi.saveGameState()


if __name__ == '__main__':
    game = Game()
    game.run()