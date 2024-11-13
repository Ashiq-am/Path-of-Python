import re
from sympy import Matrix
from pprint import pprint
from sympy.parsing.latex import parse_latex


def latex_to_matrix(latex_matrix: str) -> Matrix():
    """This function convert latex matrix into sympy matrix"""

    pattern = r"\\left\[\\begin\{matrix\}(.*?)\\end\{matrix\}\\right\]"
    data = re.search(pattern, latex_matrix)[1]
    rows = data.split("\\\\")
    python_matrix = []
    for row in rows:
        elements_list = row.split("&")
        python_matrix.append(elements_list)
    sympy_matrix = []
    for row in python_matrix:
        sympy_row = [parse_latex(element) for element in row]
        sympy_matrix.append(sympy_row)
    return Matrix(sympy_matrix)


input = r"\left[\begin{matrix}1 & \sqrt[4]{9} & \frac{\frac{11}{2}}{5} \\ -\frac{2}{5} & -1.8 & 2^{4} \\ g & -100 & i\end{matrix}\right]"
pprint(latex_to_matrix(input))
