import numpy as np
from pymoo.core.problem import Problem


class CostQualityOptimization(Problem):

    def __init__(self):
        super().__init__(n_var=5, n_obj=3, n_ieq_constr=0, xl=0.0, xu=1.0)

    def _evaluate(self, x, out, *args, **kwargs):
        out["F"] = np.sum((x - 0.5) ** 2, axis=1)
        out["G"] = 0.1 - out["F"]