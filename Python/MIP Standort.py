from ortools.linear_solver import pywraplp

# Initialisiere und definiere den Solver
solver = pywraplp.Solver(
    'MIP Standort', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

# PARAMETERDEFINITION

# Fixkosten
f = [10, 20, 10, 30, 12, 17]

# Transportkosten
c = [[10, 5, 10, 16, 9, 16, 14, 15],
     [16, 13, 14, 11, 7, 15, 19, 8],
     [16, 16, 11, 17, 9, 17, 16, 6],
     [15, 14, 9, 7, 7, 5, 11, 18],
     [16, 13, 9, 20, 13, 8, 10, 9],
     [13, 14, 4, 17, 8, 7, 4, 10]]

# Kapazitäten
b = [100, 70, 110, 90, 120, 75]

# Nachfragen
d = [50, 70, 55, 22, 35, 71, 90, 100]

# Anzahl Standorte
I = len(f)

# Anzahl Kunden
J = len(d)

# VARIABLENDEKLARATION
x = [[]]*I
for i in range(I):
    x[i] = [[]]*J
    for j in range(J):
        x[i][j] = solver.NumVar(0.0, solver.infinity(), "x_%s_%d" % (i, j))

y = [[]]*I
for i in range(I):
    y[i] = solver.BoolVar("y_%s" % i)


#### DEFINITION DER NEBENBEDINGUNGEN ####

# (2) Liefermenge an j >= Nachfrage j
for j in range(J):
    menge_j = []
    for i in range(I):
        menge_j.append(x[i][j])
    solver.Add(solver.Sum(menge_j) >= d[j])

# (3) Liefermenge <= Kapazität / offen
for i in range(I):
    menge_i = []
    for j in range(J):
        menge_i.append(x[i][j])
    solver.Add(sum(menge_i) <= b[i]*y[i])


# DEFINITION DER ZIELFUNKTION
fix = []
for i in range(I):
    fix.append(f[i]*y[i])

transport = []
for i in range(I):
    for j in range(J):
        transport.append(c[i][j] * x[i][j])
solver.Minimize(sum(fix) + sum(transport))

# TRIGGERN DES LÖSUNGSVORGANGS
status = solver.Solve()


# AUSGABE DER LÖSUNG
print('Number of variables =', solver.NumVariables())
print('Number of constraints =', solver.NumConstraints())

if status == pywraplp.Solver.OPTIMAL:
    print('Lösung:')
    print('Zielfunktionswert =', solver.Objective().Value())
    for i in range(I):
        for j in range(J):
            if x[i][j].solution_value() > 0:
                print('Liefermenge von Standort ', i,
                      ' and Kunde ', j, ' = ', x[i][j].solution_value())

else:
    print('Keine Lösung gefunden')

# AUSGABE DER LÖSUNGSZEIT UND ANGABEN ZUM LÖSUNGSVORGANG
print('\nLösungsvorgang:')
print('Problem solved in %f milliseconds' % solver.wall_time())
print('Problem solved in %d iterations' % solver.iterations())
print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
