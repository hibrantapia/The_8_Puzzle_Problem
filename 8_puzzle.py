from simpleai.search import SearchProblem, astar

# Define el estado inicial del rompecabezas
initial_state = (4, 3, 2, 1, 5, 6, 7, 8, 0)

# Define el estado final que deseamos del rompecabezas
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Definir la función heurística utilizando la cantidad de elementos que están en la posición incorrecta o en este caso la NO FINAL
def heuristic(state):
    distance = 0
    for i in range(0, 9):
        if state.index(i) != goal_state.index(i):
            distance += 1
    return distance

# Define el problema del rompecabezas como un objeto SearchProblem
class PuzzleProblem(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def actions(self, state):
        actions = []
        i = state.index(0)
        if i % 3 != 0:
            actions.append(('izquierda', i, i-1))
        if i % 3 != 2:
            actions.append(('derecha', i, i+1))
        if i // 3 != 0:
            actions.append(('arriba', i, i-3))
        if i // 3 != 2:
            actions.append(('abajo', i, i+3))
        return actions

    def result(self, state, action):
        state = list(state)
        state[action[1]], state[action[2]] = state[action[2]], state[action[1]]
        return tuple(state)

    def is_goal(self, state):
        return state == goal_state

    def heuristic(self, state):
        return heuristic(state)

# Resuelve el rompecabezas usando el algoritmo A*
problem = PuzzleProblem(initial_state)
result = astar(problem, graph_search=True)

# Imprime la solución
for action, state in result.path():
    print('Mueve', action)
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()