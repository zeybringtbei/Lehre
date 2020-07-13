from ortools.linear_solver import pywraplp


# Initialisiere und definiere den Solver
solver = pywraplp.Solver(
    'Deckungsbeitrag_lang', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)


# PARAMETERDEFINITION
X_1_max = 1
X_2_max = 1
X_3_max = 7
C = 5
d_1 = 18
d_2 = 8
d_3 = 2.6
c_1 = 3.3
c_2 = 1.5
c_3 = 0.5


# VARIABLENDEKLARATION
x_1 = solver.IntVar(0.0, solver.infinity(),  "x_1")
x_2 = solver.IntVar(0.0, solver.infinity(),  "x_2")
x_3 = solver.IntVar(0.0, solver.infinity(),  "x_3")

#### DEFINITION DER NEBENBEDINGUNGEN ####

# X_max
solver.Add(x_1 <= X_1_max)
solver.Add(x_2 <= X_2_max)
solver.Add(x_3 <= X_3_max)

# Kapazitätsverbrauch
solver.Add(c_1 * x_1 + c_2 * x_2 + c_3 * x_3 <= C)

# DEFINITION DER ZIELFUNKTION
solver.Maximize(d_1 * x_1 + d_2 * x_2 + d_3 * x_3)

# TRIGGERN DES LÖSUNGSVORGANGS
status = solver.Solve()


# AUSGABE DER LÖSUNG
print('Anzahl Variablen =', solver.NumVariables())
print('Anzahl Nebenbedingungen =', solver.NumConstraints())

if status == pywraplp.Solver.OPTIMAL:
    print('Lösung:')
    print('Zielfunktionswert =', solver.Objective().Value())
    print('x_1 =', x_1.solution_value())
    print('x_2 =', x_2.solution_value())
    print('x_3 =', x_3.solution_value())
else:
    print('The problem does not have an optimal solution.')

# AUSGABE DER LÖSUNGSZEIT UND ANGABEN ZUM LÖSUNGSVORGANG
print('\nLösungsvorgang:')
print('Problem solved in %f milliseconds' % solver.wall_time())
print('Problem solved in %d iterations' % solver.iterations())
print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
