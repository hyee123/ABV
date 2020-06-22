import sys

class loadout:
    def __init__(self,name):
        self.name = name
        self.drinkers = {}
    
    def addDrinkers(self):
        for line in sys.stdin:
            line = line.rstrip("\n")
            if line == "done":
                break
            print("Type Name and then Return. When finished type 'done'")
            self.drinkers[line] = drinker(line)


    def __str__(self):
        return str(self.drinkers)

    def toScreen(self):
        for key in self.drinkers:
            print(key +":" + str(self.drinkers[key].drinks))

class drinker:
    def __init__(self,name):
        self.name = name
        self.drinks = 0
        
    def __str__(self):
        return str(self.drinks)


def main():

    startup()

    curLoad = loadout("New Load")
    curLoad.addDrinkers()
    for line in sys.stdin:
        line = line.rstrip("\n")
        

        if line == "exit" or line == "quit":
            break
        

        
        

        
        print(line)        
        
    curLoad.toScreen()

def startup():
    print("\n\n\n\n\n\nWELCOME TO ABV")
    print("-------------")

if __name__ == "__main__":
    main()
