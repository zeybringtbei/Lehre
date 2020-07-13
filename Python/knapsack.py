from ortools.linear_solver import pywraplp

# Initialisiere und definiere den Solver
solver = pywraplp.Solver(
    'Knapsack', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

# PARAMETERDEFINITION
v = [2, 9, 10, 7, 6, 8, 4, 6, 12]
w = [3, 4, 5, 7, 8, 12, 4, 7, 13]
C = 15

# Anzahl Produkte (hier: 9)
n = len(v)

# VARIABLENDEKLARATION
x = [[]]*n
for i in range(n):
    x[i] = solver.BoolVar("x_%s" % i)


#### DEFINITION DER NEBENBEDINGUNGEN ####
weight = []
for i in range(n):
    weight.append(w[i]*x[i])
solver.Add(solver.Sum(weight) <= C)


# DEFINITION DER ZIELFUNKTION
value = []
for i in range(n):
    value.append(v[i]*x[i])
solver.Maximize(sum(value))

# TRIGGERN DES LÖSUNGSVORGANGS
status = solver.Solve()


# AUSGABE DER LÖSUNG
print('Number of variables =', solver.NumVariables())
print('Number of constraints =', solver.NumConstraints())

if status == pywraplp.Solver.OPTIMAL:
    print('Lösung:')
    print('Zielfunktionswert =', solver.Objective().Value())
    print("x = ", [x[i].solution_value() for i in range(n)])
else:
    print('Keine Lösung gefunden')

# AUSGABE DER LÖSUNGSZEIT UND ANGABEN ZUM LÖSUNGSVORGANG
print('\nLösungsvorgang:')
print('Problem solved in %f milliseconds' % solver.wall_time())
print('Problem solved in %d iterations' % solver.iterations())
print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
