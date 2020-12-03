from ortools.linear_solver import pywraplp
from colorama import Style, Fore


# Initialisiere und definiere den Solver
solver = pywraplp.Solver(
    "SetCover", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

# PARAMETER
H = ["Aachen", "Essen", "Bielefeld", "Paderborn", "Bochum", "Leverkusen",
     "Düsseldorf", "Münster", "Gütersloh", "Lippstadt", "Wuppertal", "Dortmund",
     "Delbrück", "Duisburg", "Köln", "Mönchengladbach", "Lemgo", "Bonn"]

S = ["Köln", "Düsseldorf", "Dortmund", "Münster", "Bielefeld", "Paderborn"]

S_h ={
    "Aachen": ["Köln"], 
    "Essen": ["Dortmund"], 
    "Bielefeld": ["Münster", "Bielefeld"], 
    "Paderborn": ["Bielefeld", "Paderborn"], 
    "Bochum": ["Dortmund"], 
    "Leverkusen": ["Köln", "Düsseldorf"], 
    "Düsseldorf": ["Köln", "Düsseldorf"], 
    "Münster": ["Münster", "Bielefeld"], 
    "Gütersloh": ["Münster", "Bielefeld"], 
    "Lippstadt": ["Paderborn"], 
    "Wuppertal": ["Düsseldorf", "Dortmund"], 
    "Dortmund": ["Dortmund"], 
    "Delbrück": ["Paderborn"], 
    "Duisburg": ["Düsseldorf", "Dortmund"], 
    "Köln": ["Köln"], 
    "Mönchengladbach": ["Köln", "Düsseldorf"], 
    "Lemgo": ["Bielefeld"], 
    "Bonn": ["Köln"]
}


# VARIABLENDEKLARATION
x = [[]]*len(S)
for s in range(len(S)):
    x[s]= solver.BoolVar("x_{}".format(s))


#### DEFINITION DER NEBENBEDINGUNG ####

# (1) Beliefern
for h in H:
    solver.Add(solver.Sum([x[S.index(s)] for s in S_h[h]]) >= 1)

# Zielfunktion
solver.Minimize(sum([x[S.index(s)] for s in S]))


# TRIGGERN DES LÖSUNGSVORGANGS
status= solver.Solve()


# AUSGABE DER LÖSUNG
print(f"\n----------------------------------------")
print(Style.BRIGHT + "Modell" + Style.RESET_ALL)
print("Anzahl Variablen =", solver.NumVariables())
print("Anzahl Nebenbedingungen =", solver.NumConstraints())
print(f"----------------------------------------")
if status == pywraplp.Solver.OPTIMAL:
    print(Style.BRIGHT + Fore.GREEN +"Lösung:"+ Style.RESET_ALL)
    print("Zielfunktionswert = {} eröffnete Standorte".format(solver.Objective().Value()))
    for s in range(len(S)):
        if x[s].solution_value() > 0.5:
            print("{} wird eröffnet".format(S[s]))
    

else:
    print("Keine Lösung gefunden")
print(f"----------------------------------------")
# AUSGABE DER LÖSUNGSZEIT UND ANGABEN ZUM LÖSUNGSVORGANG
print(Style.BRIGHT +"Lösungsvorgang:" + Style.RESET_ALL)
print("Lösungszeit in %f Millisekunden" % solver.wall_time())
print("Problem solved in %d iterations" % solver.iterations())
print("Problem solved in %d branch-and-bound nodes" % solver.nodes())
print(f"----------------------------------------\n")