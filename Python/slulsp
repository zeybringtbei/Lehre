from ortools.linear_solver import pywraplp
import random


def random_instance(perioden=4, untergrenze=10, obergrenze=100):
    return [random.randint(untergrenze, obergrenze) for _ in range(perioden)]


    # Initialisiere und definiere den Solver
solver = pywraplp.Solver(
    'SLULSP', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)


# PARAMETERDEFINITION
d = [20, 10, 30, 10]
# Für Zufallsinstanz ent-kommentieren
# d = random_instance(perioden=100, untergrenze=10, obergrenze=100)
l = 1
s = 20
M = sum(d)
T = len(d)


# VARIABLENDEKLARATION
L = [[]]*T
X = [[]]*T
y = [[]]*T

for t in range(T):
    L[t] = solver.NumVar(0.0, solver.infinity(),  "L_%s" % (t))
    X[t] = solver.NumVar(0.0, solver.infinity(), "")
    y[t] = solver.BoolVar("")


#### DEFINITION DER NEBENBEDINGUNGEN ####

# (2) Lagerbilanzgleichung

# Erste Periode (ohne Anfangslagerbestand)
solver.Add(X[0] - d[0] == L[0])
# Alle anderen Perioden
# (unter Berücksichtigung des Lagerendbestands der Vorperiode)
for t in range(1, T):
    solver.Add(L[t-1]+X[t]-d[t] == L[t])

# (3) Rüstrestriktion
for t in range(T):
    solver.Add(X[t] <= y[t]*M)

# DEFINITION DER ZIELFUNKTION
objective = solver.Objective()
for t in range(T):
    # Multipliziert L[t] mit l und fügt ein "+" hinter
    objective.SetCoefficient(L[t], l)
    # Multipliziert y[t] mit s und fügt ein "+" hinter
    objective.SetCoefficient(y[t], s)
objective.SetMinimization()

# TRIGGERN DES LÖSUNGSVORGANGS
status = solver.Solve()


# AUSGABE DER LÖSUNG
print('Number of variables =', solver.NumVariables())
print('Number of constraints =', solver.NumConstraints())

if status == pywraplp.Solver.OPTIMAL:
    print('Lösung:')
    print('Zielfunktionswert =', solver.Objective().Value())
    print('X =', [X[t].solution_value() for t in range(T)])
    print('y =', [y[t].solution_value() for t in range(T)])
    print("L =", [L[t].solution_value() for t in range(T)])
else:
    print('The problem does not have an optimal solution.')

# AUSGABE DER LÖSUNGSZEIT UND ANGABEN ZUM LÖSUNGSVORGANG
print('\nAdvanced usage:')
print('Problem solved in %f milliseconds' % solver.wall_time())
print('Problem solved in %d iterations' % solver.iterations())
print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
