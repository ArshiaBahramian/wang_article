import numpy as np
from pymoo.optimize import minimize
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.operators.mutation.bitflip import BitflipMutation
from pymoo.util.ref_dirs import get_reference_directions
import networkx as nx
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.sampling.rnd import BinaryRandomSampling
from criticalpath import CriticalPath
from pymoo.termination import get_termination
from pymoo.termination.default import DefaultMultiObjectiveTermination
import matplotlib.pyplot as plt


class ConstructionSchedulingProblem(ElementwiseProblem):
    def __init__(self, w, c, q):
        n_activities = 20
        super().__init__(n_var=n_activities * 3, n_obj=3, n_constr=0, xl=0, xu=1, elementwise_evaluation=True)
        self.w = w
        self.c = c
        self.q = q
        self.n_activities = n_activities

    def _evaluate(self, x, out, *args, **kwargs):
        x_bin = x.reshape(self.n_activities, 3)
        total_cost = np.sum([self.c[j][m] * x_bin[j, m] for j in range(self.n_activities) for m in range(3)])
        total_quality = np.sum(
            [self.w[j] * self.q[j][m] * x_bin[j, m] for j in range(self.n_activities) for m in range(3)])
        durations = {str(i + 1): np.dot(x_bin[i], [1, 2, 3]) for i in range(self.n_activities)}
        cp = CriticalPath(durations)
        duration = cp.calculate_critical_path()
        out["F"] = [duration, total_cost, -total_quality]
        print(x)
        print(len(x))


w = np.random.rand(20)
c = [np.random.rand(3) for _ in range(20)]
q = [np.random.rand(3) for _ in range(20)]

problem = ConstructionSchedulingProblem(w, c, q)

ref_dirs = get_reference_directions("das-dennis", 3, n_partitions=12)
algorithm = NSGA3(pop_size=500,
                  n_offsprings=500,
                  sampling=BinaryRandomSampling(),
                  crossover=SBX(prob=0.8, eta=15),
                  mutation=BitflipMutation(prob=0.1),
                  eliminate_duplicates=True,
                  ref_dirs=ref_dirs
                  )
termination = get_termination("n_gen", 1)
# termination = DefaultMultiObjectiveTermination(
#     xtol=1e-8,
#     cvtol=1e-6,
#     ftol=0.0025,
#     period=30,
#     n_max_gen=10000,
#     n_max_evals=100000
# )

res = minimize(problem, algorithm, termination, seed=1, save_history=True, verbose=True)
X = res.X
F = res.F



# xl, xu = problem.bounds()
# plt.figure(figsize=(7, 5))
# plt.scatter(X[:, 0], X[:, 1], s=30, facecolors='none', edgecolors='r')
# plt.xlim(xl[0], xu[0])
# plt.ylim(xl[1], xu[1])
# plt.title("Design Space")
# plt.show()