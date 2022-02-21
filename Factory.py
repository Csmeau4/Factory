import time

class Task:
    def __init__(self,name,exectime,cd,onrun,oiladd,oilneed,wheeladd,engineadd):
        self.name = name
        self.exectime = exectime
        self.cd = cd
        self.currentcd = 0
        self.onrun = onrun

        self.oiladd = oiladd
        self.oilneed = oilneed
        self.wheeladd = wheeladd
        self.engineadd = engineadd

    def run(self,currentoil):
        if self.currentcd == 0:
            if currentoil >= self.oilneed:
                print(self.name + " RAN")
                self.currentcd = self.cd
                return True
            else:
                print(self.name + " COULDN'T RUN, OIL")
                return False
        else:
            print(self.name + " COULDN'T RUN, CD")
            return False

    def tickdown(self,time):
        self.currentcd = self.currentcd - time
        if self.currentcd < 0:
            self.currentcd = 0

def factory():
    tank = 0
    wheel = 0
    engine = 0
    kit = 0
    runtime = 0

    tasklist = []
    tasklist.append(
        Task("Pump 2", 3, 15,     "Oil     +20", 20, 0, 0, 0))
    tasklist.append(
        Task("Pump 1",    2,  5,  "Oil     +10", 10,  0,  0,  0))
    tasklist.append(
        Task("Machine 1", 5,  5,  "Engine  +1",   0, 25,  0,  1))
    tasklist.append(
        Task("Machine 2", 3,  5,  "Wheel   +1",   0,  5,  1,  0))

    runtask = 0
    while runtime < 120:
        time.sleep(0.5)


        """
            Surplus dans le réservoir, élimination
        """
        if tank > 50:
            tank = 50

        """
            Construction d'une voiture si les matériaux sont disponibles
        """

        if wheel >= 4 and engine >= 1:
            kit += 1
            wheel -= 4
            engine -= 1

        """
            Choix de la tâche à run:
            
            Détermination de la liste de tâches possibles
        """
        runnable = []
        taskindex = 0
        for task in tasklist:
            if task.currentcd == 0 and task.oilneed <= tank:
                runnable.append(taskindex)
            taskindex += 1

        #Si une seule tâche possible, run celle là
        wait = False
        if 3 in runnable:
            runtask = 3
        elif 0 in runnable or 1 in runnable:
            runtask = runnable[0]
        elif runnable.__len__() == 1 and engine == 0:
            runtask = runnable[0]
        else:
            runtask = -1
            wait = True




        """
            Execution de la tâche choisie, ajout et retrait des valeurs
        """
        if not wait and tasklist[runtask].run(tank):
            tank -= tasklist[runtask].oilneed
            tank += tasklist[runtask].oiladd
            wheel += tasklist[runtask].wheeladd
            engine += tasklist[runtask].engineadd
            timespent = tasklist[runtask].exectime
            couldrun = True

        else:
            timespent = 1
            couldrun = False
        wait = False

        runtime += timespent
        """
            Refroidissement de chacune des tâches, SAUF CELLE QUI VIENT DE RUN
        """
        for x in range(0, 4):
            if runtask != x or not couldrun:
                tasklist[x].tickdown(timespent)

        """
            Ajout du temps de la tâche à l'exécution, qu'elle aie run ou pas
        """

        print(tank, wheel, engine, runtime, kit)









if __name__ == '__main__':
    factory()


