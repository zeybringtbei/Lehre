from ortools.linear_solver import pywraplp

# Initialisiere und definiere den Solver
solver = pywraplp.Solver(
    'Deckungsbeitrag_kurz', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

# PARAMETERDEFINITION
X_max = [1, 1, 7]
C = 5
d = [18, 8, 2.6]
c = [3.3, 1.5, 0.5]
# Anzahl Produkte (hier: 3)
nr_x = len(d)

# VARIABLENDEKLARATION
# X_max als jew. Maximalwert, den die Variable annehmen kann, an
x = [[]]*nr_x
for i in range(nr_x):
    x[i] = solver.IntVar(0.0, X_max[i],  "x_%s" % i)


#### DEFINITION DER NEBENBEDINGUNGEN ####
kap_verbrauch = []
for i in range(nr_x):
    kap_verbrauch.append(c[i]*x[i])
solver.Add(solver.Sum(kap_verbrauch) <= C)


# DEFINITION DER ZIELFUNKTION
deckungs_beitrag = []
for i in range(nr_x):
    deckungs_beitrag.append(d[i]*x[i])
solver.Maximize(sum(deckungs_beitrag))

# TRIGGERN DES LÖSUNGSVORGANGS
status = solver.Solve()


# AUSGABE DER LÖSUNG
print('Number of variables =', solver.NumVariables())
print('Number of constraints =', solver.NumConstraints())

if status == pywraplp.Solver.OPTIMAL:
    print('Lösung:')
    print('Zielfunktionswert =', solver.Objective().Value())
    print("x=", [x[i].solution_value() for i in range(nr_x)])
else:
    print('Keine Lösung gefunden')

# AUSGABE DER LÖSUNGSZEIT UND ANGABEN ZUM LÖSUNGSVORGANG
print('\nLösungsvorgang:')
print('Problem solved in %f milliseconds' % solver.wall_time())
print('Problem solved in %d iterations' % solver.iterations())
print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
