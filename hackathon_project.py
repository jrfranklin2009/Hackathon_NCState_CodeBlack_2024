import tkinter as tk
import turtle as t

class ask_for_num_animals:
    def __init__(self):
        self.ask_for_num_animals_window = tk.Tk()
        self.ask_for_num_animals_window.geometry("2100x1800")
        self.ask_for_num_animals = tk.Label(text = "How many animals will you input data for?", font=('Arial', 12, 'normal')).pack()

        self.num_animals = tk.Entry(text = "")
        self.num_animals.pack()
        self.nextButton = tk.Button(text = "Next",width = 25, height = 5, bg = "Grey", fg = "White", command = self.saveNumAnimalsEntryAndExit).pack()
        self.ask_for_num_animals_window.mainloop()

    
    def saveNumAnimalsEntryAndExit(self):
        if self.num_animals.get() != "" and float(self.num_animals.get()) > 0 and float(self.num_animals.get())%1 == 0:
            self.data = self.num_animals.get()
            self.ask_for_num_animals_window.destroy()

            ask_for_birth_time_class = ask_for_birth_time(self.data)
            del self
        else:
            pass

class ask_for_birth_time:
    def __init__(self, numTimesToAsk):
        self.numTimesToAsk = int(numTimesToAsk)
        self.entryTimes = []
        for i in range(self.numTimesToAsk):
            self.ask_for_birth_time_window = tk.Tk()
            self.ask_for_birth_time_window.geometry("2100x1800")
            askForBirthYearClass( self.ask_for_birth_time_window,i+1, self)
        self.ask_for_birth_time_window = tk.Tk()
        self.ask_for_birth_time_window.geometry("2100x1800")
        self.label = tk.Label(text = "Click to input the year at which the animal reaches maturity.",font=('Arial', 12, 'normal'))
        self.label.pack()
        self.nextButton = tk.Button(text = "Next", width = 25, height = 5, bg = "Grey", fg = "White", command = self.saveBirthTimesAndExit)
        self.nextButton.pack()
        self.ask_for_birth_time_window.mainloop()


    def saveBirthTimesAndExit(self):
        self.nextButton.destroy()
        self.label.destroy()
        self.ask_for_birth_time_window.destroy()
        ask_for_maturity_time_class = ask_for_maturity_time(self.entryTimes)
        del self


class askForBirthYearClass:
    def __init__(self, window, animalAskNum, master):
        self.window = window
        self.window.geometry("2100x1800")
        self.masterClass = master
        self.birthLabel = tk.Label(text = "What year was animal " + str(animalAskNum) + " born?", font=('Arial', 12, 'normal'))
        self.birthLabel.pack()
        self.entryAsk = tk.Entry()
        self.entryAsk.pack()
        self.nextButton = tk.Button(text = "Next", width = 25, height = 5, bg = "Grey", fg = "White", command = self.saveBirthYearAndExit)
        self.nextButton.pack()
        self.window.mainloop()
    def saveBirthYearAndExit(self):
        if self.entryAsk.get() != "" and int(self.entryAsk.get())>1500:
            self.birthYear = self.entryAsk.get()
            self.entryAsk.destroy()
            self.nextButton.destroy()
            self.birthLabel.destroy()
            self.window.destroy()
            self.masterClass.entryTimes.append(self.birthYear)
            del self

class ask_for_maturity_time:
    def __init__(self, birthdates):
        self.numTimesToAsk = len(birthdates)
        self.birthdateList = birthdates
        self.entryMaturityTimes = []
        for i in range(self.numTimesToAsk):
            self.ask_for_maturity_time_window = tk.Tk()
            self.ask_for_maturity_time_window.geometry("2100x1800")
            askForMaturityYearClass(self.ask_for_maturity_time_window, i+1, self)
            self.ask_for_maturity_time_window = tk.Tk()
            self.ask_for_maturity_time_window.geometry("2100x1800")
            self.ask_for_maturity_time_window.destroy()
        self.ask_for_maturity_time_window = tk.Tk()
        self.ask_for_maturity_time_window.geometry("2100x1800")
        self.label = tk.Label(text = "Click to input the year at which the animal dies.", font=('Arial', 12, 'normal'))
        self.label.pack()
        self.nextButton= tk.Button(text = "Next", width = 25, height = 5, bg = "Grey", fg = "White", command = self.saveMaturityTimesAndExit)
        self.nextButton.pack()
        self.ask_for_maturity_time_window.mainloop()

    def saveMaturityTimesAndExit(self):
        self.nextButton.destroy()
        self.label.destroy()
        self.ask_for_maturity_time_window.destroy()
        ask_for_death_time_class = ask_for_death_time(self.birthdateList, self.entryMaturityTimes)
        del self

class askForMaturityYearClass:
    def __init__(self, window, animalAskNum, master):
        self.window = window
        self.window.geometry("2100x1800")
        self.masterClass = master
        self.askNum = int(animalAskNum)-1
        self.maturityLabel = tk.Label(text = "What year did animal " + str(int(self.askNum)+1) + " reach maturity (became an adult)?",font=('Arial', 12, 'normal'))
        self.maturityLabel.pack()
        self.entryAsk = tk.Entry()
        self.entryAsk.pack()
        self.nextButton = tk.Button(text="Next", width = 25, height = 5, bg = "Grey", fg = "White", command = self.saveMaturityYearAndExit)
        self.nextButton.pack()
        self.window.mainloop()
    def saveMaturityYearAndExit(self):
        if self.entryAsk.get() != "" and int(self.entryAsk.get())>1500 and int(self.entryAsk.get())>int(self.masterClass.birthdateList[int(self.askNum)]):
            self.maturityYear = self.entryAsk.get()
            self.masterClass.entryMaturityTimes.append(self.maturityYear)
            self.entryAsk.destroy()
            self.nextButton.destroy()
            self.window.destroy()
            del self

class ask_for_death_time:
    def __init__(self, birthdates, maturitydates):
        self.numTimesToAsk = len(birthdates)
        self.birthdateList = birthdates
        self.maturitydateList = maturitydates
        self.entryDeathTimes = []
        for i in range(self.numTimesToAsk):
            self.ask_for_death_time_window = tk.Tk()
            self.ask_for_death_time_window.geometry("2100x1800")
            askForDeathYearClass(self.ask_for_death_time_window, i + 1, self)
            self.ask_for_death_time_window = tk.Tk()
            self.ask_for_death_time_window.geometry("2100x1800")
            self.ask_for_death_time_window.destroy()
        self.ask_for_death_time_window = tk.Tk()
        self.ask_for_death_time_window.geometry("2100x1800")
        self.label = tk.Label(text = "Click to see analysis.", font=('Arial', 12, 'normal'))
        self.label.pack()
        self.nextButton = tk.Button(text = "Next", width = 25, height = 5, bg = "Grey", fg = "White", command = self.saveDeathTimesAndExit)
        self.nextButton.pack()
        self.ask_for_death_time_window.mainloop()
    def saveDeathTimesAndExit(self):
        self.nextButton.destroy()
        self.label.destroy()
        self.ask_for_death_time_window.destroy()
        present_results_class = presents_results(self.birthdateList, self.maturitydateList, self.entryDeathTimes)
        del self

class askForDeathYearClass:
    def __init__(self, window, animalAskNum, master):
        self.window = window
        self.window.geometry("2100x1800")
        self.masterClass = master
        self.myAskNum = int(animalAskNum)-1
        self.dieLabel = tk.Label(text = "What year did animal " + str(int(self.myAskNum)+1) + " die?",font=('Arial', 12, 'normal'))
        self.dieLabel.pack()
        self.entryAsk = tk.Entry()
        self.entryAsk.pack()
        self.nextButton = tk.Button(text = "Next", width = 25, height = 5, bg = "Grey", fg = "White", command = self.saveDeathYearAndExit)
        self.nextButton.pack()
        self.window.mainloop()
    def saveDeathYearAndExit(self):
        if self.entryAsk.get() != "" and int(self.entryAsk.get())>1500 and int(self.entryAsk.get())>int(self.masterClass.maturitydateList[self.myAskNum]):
            self.deathYear = self.entryAsk.get()
            self.masterClass.entryDeathTimes.append(self.deathYear)
            self.entryAsk.destroy()
            self.nextButton.destroy()
            self.window.destroy()
            del self

class presents_results:
    def __init__(self, birthdateList, maturitydateList, deathdateList):
        birthdateListSum = 0
        for i in birthdateList:
            birthdateListSum += float(i)
        averagebirthdate = birthdateListSum/len(birthdateList)
        deathdateListSum = 0
        for i in deathdateList:
            deathdateListSum += float(i)
        averagedeathdate = deathdateListSum/len(deathdateList)
        maturityListSum = 0
        for i in maturitydateList:
            maturityListSum += float(i)
        averagematuritydate = maturityListSum/len(maturitydateList)
        averageage = averagedeathdate - averagebirthdate
        averagetimetillmaturity = averagematuritydate - averagebirthdate
        presentTurtle = t.Turtle()
        presentTurtle.hideturtle()
        presentTurtle.penup()
        presentTurtle.speed(0)
        presentScreen = t.Screen()
        presentScreen.setup(width=1.0,height=1.0)
        presentTurtle.goto(-400,375)
        presentTurtle.write("The average age of this species is " + str(round(averageage,ndigits = 2)) + " years.", font = ('Arial', 20, 'normal'))
        presentTurtle.goto(-400,300)
        presentTurtle.write("The average time it takes for this species to reach maturity is " + str(round(averagetimetillmaturity,ndigits = 2)) + " years.", font = ('Arial', 20, 'normal'))
        if 1< len(birthdateList) < 5:
            presentTurtle.goto(-650, -375)
            presentTurtle.pendown()
            presentTurtle.goto(-650,75)
            presentTurtle.write("Age (yrs)")
            presentTurtle.goto(-650,-375)
            presentTurtle.goto(-200,-375)
            presentTurtle.write("Turtles")
            presentTurtle.goto(-650,-375)
            for i in range(len(birthdateList)):
                presentTurtle.goto(-650+(i+1)*(450/(len(birthdateList)+2)),-375)
                presentTurtle.goto(-650+(i+1)*(450/(len(birthdateList)+2))-5,-375)
                presentTurtle.begin_fill()
                presentTurtle.goto(-650+(i+1)*(450/(len(birthdateList)+2))-5,(1-(((int(deathdateList[i])-int(birthdateList[i]))/(averageage*5))))*(-375)+200)
                presentTurtle.goto(-650+(i+1)*(450/(len(birthdateList)+2))+5,(1-(((int(deathdateList[i])-int(birthdateList[i]))/(averageage*5))))*(-375)+200)
                presentTurtle.write("Age: " + str(int(deathdateList[i])-int(birthdateList[i]))+" years.")
                presentTurtle.goto(-650+(i+1)*(450/(len(birthdateList)+2))+5,-375)
                presentTurtle.goto(-650+(i+1)*(450/(len(birthdateList)+2))-5,-375)
                presentTurtle.end_fill()
            presentTurtle.goto(-650+(len(birthdateList)+1)*(450/(len(birthdateList)+2)),-375)
            presentTurtle.goto(-650+(len(birthdateList)+1)*(450/(len(birthdateList)+2))-5,-375)
            presentTurtle.begin_fill()
            presentTurtle.goto(-650+(len(birthdateList)+1)*(450/(len(birthdateList)+2))-5,(1-((1/(5))))*(-375)+200)
            presentTurtle.goto(-650+(len(birthdateList)+1)*(450/(len(birthdateList)+2))+5,(1-((1/(5))))*(-375)+200)
            presentTurtle.write("Average age: " + str(round(averageage,ndigits=2))+" years.", font = ('Arial',8,'normal'))
            presentTurtle.goto(-650+(len(birthdateList)+1)*(450/(len(birthdateList)+2))+5,-375)
            presentTurtle.goto(-650+(len(birthdateList)+1)*(450/(len(birthdateList)+2))-5,-375)
            presentTurtle.end_fill()
            presentTurtle.penup()
            presentTurtle.goto(767.5-650, -375)
            presentTurtle.pendown()
            presentTurtle.goto(767.5-650,0)
            presentTurtle.write("Time untill maturity (yrs)")
            presentTurtle.goto(767.5-650,-375)
            presentTurtle.goto(767.5-275,-375)
            presentTurtle.write("Turtles")
            presentTurtle.goto(767.5-650,-375)
            for i in range(len(birthdateList)):
                presentTurtle.goto(767.5-(-(-650+(i+1)*(375/(len(birthdateList)+2)))),-375)
                presentTurtle.goto(767.5-(-(-650+(i+1)*(375/(len(birthdateList)+2))-5)),-375)
                presentTurtle.begin_fill()
                presentTurtle.goto(767.5-(-(-650+(i+1)*(375/(len(birthdateList)+2))-5)),(1-(((int(maturitydateList[i])-int(birthdateList[i]))/(averagetimetillmaturity*5))))*(-375)+200)
                presentTurtle.goto(767.5-(-(-650+(i+1)*(375/(len(birthdateList)+2))+5)),(1-(((int(maturitydateList[i])-int(birthdateList[i]))/(averagetimetillmaturity*5))))*(-375)+200)
                presentTurtle.write(str(int(maturitydateList[i])-int(birthdateList[i]))+" years untill maturity.", font = ('Arial',7,'normal'))
                presentTurtle.goto(767.5-(-(-650+(i+1)*(375/(len(birthdateList)+2))+5)),-375)
                presentTurtle.goto(767.5-(-(-650+(i+1)*(375/(len(birthdateList)+2))-5)),-375)
                presentTurtle.end_fill()
            presentTurtle.goto(767.5-(-(-650+(len(birthdateList)+1)*(375/(len(birthdateList)+2)))),-375)
            presentTurtle.goto(767.5-(-(-650+(len(birthdateList)+1)*(375/(len(birthdateList)+2))-5)),-375)
            presentTurtle.begin_fill()
            presentTurtle.goto(767.5-(-(-650+(len(birthdateList)+1)*(375/(len(birthdateList)+2))-5)),(1-((1/(5))))*(-375)+200)
            presentTurtle.goto(767.5-(-(-650+(len(birthdateList)+1)*(375/(len(birthdateList)+2))+5)),(1-((1/(5))))*(-375)+200)
            presentTurtle.write(str(round(averagetimetillmaturity,ndigits=2))+" years untill maturity.",font = ('Arial',7,'normal'))
            presentTurtle.goto(767.5-(-(-650+(len(birthdateList)+1)*(375/(len(birthdateList)+2))+5)),-375)
            presentTurtle.goto(767.5-(-(-650+(len(birthdateList)+1)*(375/(len(birthdateList)+2))-5)),-375)
            presentTurtle.end_fill()
def run_program():
    window = tk.Tk()
    window.geometry("2100x1800")
    greeting = tk.Label(text = "Hello!  Welcome to the animal life cycle analyzer.  \nThis program will help analyze the life cycle of an animal.  \nInput various data gathered about the life cycle of one or more animals and watch the program analyze the life cycle of the data about the species given.  \n Click Next to continue")
    greeting.pack()

    nextButton = tk.Button(text = "Next",width = 25, height = 5, bg = "Grey", fg = "White", command = window.destroy)
    nextButton.pack()

    window.mainloop()
    ask_for_animals_class = ask_for_num_animals()

run_program()
