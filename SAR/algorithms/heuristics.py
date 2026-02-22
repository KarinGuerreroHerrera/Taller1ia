from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    # TODO: Add your code here
    coordenadasObjetivo= problem.goal
    return abs(state[0] - coordenadasObjetivo[0]) + abs(state[1] - coordenadasObjetivo[1])


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    coordenadasObjetivo= problem.goal
    return ((state[0]-coordenadasObjetivo[0])**2 +(state[1] -coordenadasObjetivo[1])**2)**0.5


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    Version inicial del codigo(antes de usar la IA): 
    Estaba usando mal el minimo y no tenia bien escrita la formula de la distancia

    position= state[0] 
    survivors_grid= state[1]
    position_surv = []

    if survivors_grid.count()== 0:
        return 0

    for x in range(survivors_grid.width):
        for y in range(survivors_grid.height):
            if survivors_grid[x][y]:
                position_surv.append((x, y))

    for surv in position_surv:
        dist = min(position[0] - surv[0] + position[1] - surv[1])

    return dist

    Prompts:
    1. que es una heuristica y como puedo construir una para grid?
    2. que es y como funciona la distancia manhatan y como se calcula para distintas posiciones
    3. la formula para la distancia esta bien traducida en el codigo? dist = min(position[0]-surv[0] + position[1]-surv[1])
    4. como probar la heuristica si tengo A* y layouts en el proyecto
    """
    # TODO: Add your code here
    position, survivors_grid= state
    position_surv= []
    if survivors_grid.count()== 0:
        return 0
    
    for x in range(survivors_grid.width):
        for y in range(survivors_grid.height):
            if survivors_grid[x][y]:
                position_surv.append((x,y))

    min_dist= float('inf')
    for surv in position_surv:
        dist= abs(position[0]-surv[0])+ abs(position[1]-surv[1])
        min_dist= min(min_dist, dist)
    return min_dist
