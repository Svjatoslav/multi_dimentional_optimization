from multidimensional_problem import N_D_Problem
from Trial_Point_Method_file import trial_point_method
from golden_egg import golden_search
import matplotlib.pyplot as plot


pr1 = N_D_Problem()
pr1.nabla_calculate()  # ОБЯЗАТЕЛЬНО ЗАПУСКАТЬ В НАЧАЛЕ ПРОГРАММЫ, ЕСЛИ БУДЕМ ИСПОЛЬЗОВАТЬ СИМВОЛЬНЫЕ ВЫЧИСЛЕНИЯ

print('GOLDEN SEARCH:')
pr1.gradient_method(0.01, [5, 4], golden_search)
# pr1.draw_contoures()
pr1.graph_3d()
print(pr1.target_function([0,0]))
print('TPM:')
pr1.gradient_method(0.01, [5, 4], trial_point_method)
# pr1.graph_3d()
# pr1.draw_contoures()




