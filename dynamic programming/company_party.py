''' Rozwiązanie problemu “Impraza firmowa” tak, by zwracane były imiona pracowników, którzy idą na imprezę. 
    Pracownicy reprezentowani są w strukturze:
    class Employee:
    def __init__(self, fun, name):
    self.emp  = []
    self.fun  = fun
    self.name = name
    Wolno dokładać własne pola do struktury.
'''

class Employee:
    def __init__(self,name,fun):
        self.fun = fun
        self.name = name
        self.emp = []       # zawiera wszystkich bezposrednich podwladnych danego pracownika
        self.f = -1        # f - najlepsza impreza w poddrzewie, jesli idzie na nia employee      
        self.g = -1        # g - najlepsza impreza w poddrzewie, jezsli nie idzie na nia employee



def f(employee):
    if(employee.f >= 0):
        return employee.f

    if_going = employee.fun

    for emp in employee.emp:
       if_going += g(emp)

    if_not_going = g(employee)
    employee.f = max(if_going, if_not_going)

    return employee.f

def g(employee):
    if(employee.g >= 0):
        return employee.g

    employee.g = 0
    
    for emp in employee.emp:
        employee.g += f(emp)

    return employee.g

def get_names(arr):
    participants = []
    idx = 0
    while idx < len(arr):
        employee = arr[idx]
        if(employee.f > employee.g):
            participants.append(employee.name)
            idx += 1
            for emp in employee.emp:
                idx += 1
             
        else:
            employee.going = False
            idx += 1
            for emp in employee.emp:
                if(emp.f > emp.g):
                    participants.append(emp.name)
                    idx += 1
                else:
                    idx += 1

    return participants



magda = Employee('Magda', 10)
szymon = Employee('Szymon', 7)
pawel = Employee('Pawel', 2)
beata = Employee('Beata', 1)
sylwia = Employee('Sylwia', 8)
damian = Employee('Damian', 2)
kamil = Employee('Kamil', 1)
filip = Employee('Filip', 3)
darek = Employee('Darek', 4)

magda.emp = [szymon, pawel, beata]
szymon.emp = [sylwia, damian]
pawel.emp = [kamil]
beata.emp = [filip, darek]

arr = [magda, szymon, pawel, beata, sylwia, damian, kamil, filip, darek]

fun = f(magda)
print(fun, get_names(arr))
