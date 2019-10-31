volume = [0.000, 1.000, 2.000, 3.000, 4.000, 5.000, 6.000, 7.000,
        8.000, 9.000, 10.000, 11.000, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6,
        11.7, 11.8, 11.9, 12.0, 12.1, 12.2, 12.3,]

ph = [3.89, 4.13, 4.38, 4.57, 4.75, 4.90, 5.05, 5.21, 5.37, 
        5.56, 5.83, 6.28, 6.36, 6.44, 6.55, 6.68, 6.87, 7.15, 7.98,
        9.60, 10.07, 10.32, 10.51, 10.65, 10.75,]



def first_derivative(ind_var, dep_var):
    """Creates a list with the first derivative"""
    first_der = []
    for i in range(len(ind_var)-1):
        delta_dep_var = dep_var[i+1] - dep_var[i]
        delta_ind_var = ind_var[i+1] - ind_var[i]
        first_der.append((delta_dep_var/delta_ind_var))

    return first_der
    
def second_derivative(ind_var, dep_var):
    first_der = first_derivatve(ind_var, dep_var)
    second_der = []
    for i in range(len(first_der) - 1):
        delta_first_der = first_der[i+1] - first_der[i]
        delta_ind_var = 5 # TEMPORARY FOR SAVE




    





def scale_picker(ind_var, dep_var, vertical_squares = 18, horizontal_squares = 26):
    """"Creates a scale for graph and calculates convenient increase of variable per square"""

