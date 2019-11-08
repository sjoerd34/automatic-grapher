volume = [0.000, 1.000, 2.000, 3.000, 4.000, 5.000, 6.000, 7.000,
        8.000, 9.000, 10.000, 11.000, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6,
        11.7, 11.8, 11.9, 12.0, 12.1, 12.2, 12.3,]

ph = [3.89, 4.13, 4.38, 4.57, 4.75, 4.90, 5.05, 5.21, 5.37, 
        5.56, 5.83, 6.28, 6.36, 6.44, 6.55, 6.68, 6.87, 7.15, 7.98,
        9.60, 10.07, 10.32, 10.51, 10.65, 10.75,]



def first_derivative(ind_var, dep_var):
    """Creates a list with the first derivative"""
    first_der = []
    first_der_point = []
    for i in range(len(ind_var)-1):
        delta_dep_var = dep_var[i+1] - dep_var[i]
        delta_ind_var = ind_var[i+1] - ind_var[i]
        
        #Calculates the first derivative as change in dep_var / ind_var
        first_der.append((delta_dep_var/delta_ind_var))
        #Calculates average next and current value of ind_var
        #Because this is the point where slope is equal to first_der
        first_der_point.append((ind_var[i+1] + ind_var[i])/2)

    return [first_der, first_der_point]
    
def second_derivative(ind_var, dep_var):
    first_der = (first_derivative(ind_var, dep_var))[0]
    first_der_point = (first_derivative(ind_var, dep_var))[1]
    second_der = []
    second_der_point = []
    
    for i in range(len(first_der) - 1):
        delta_first_der = first_der[i+1] - first_der[i]
        delta_ind_var = first_der_point[i+1] - first_der_point[i]
        second_der.append(delta_first_der / delta_ind_var)
        second_der_point.append((first_der_point[i+1] + first_der_point[i])/2)
        
    return second_der

bigboy = second_derivative(volume, ph)

#for i in bigboy:
	#print(round(i, 3))

def formatter(ind_var, dep_var):
	"""formats the data the independent variable, dependent variable
	first derivative and the second derivative in a formatted table"""
	first_der = (first_derivative(ind_var, dep_var))[0]
	second_der = second_derivative(ind_var, dep_var)
	c = '-'
	b = '|'
	for i in range(len(ind_var)):
		if i == (len(ind_var)-1):
			print('{4}{0:^8}{4}{1:^8}{4}{2:^8}{4}{3:^8}{4}'.format(ind_var[i], dep_var[i], '', '', b))
			print(c*37)
		
		elif i == 0:
			print(c*37)
			print('{4}{0:^8}{4}{1:^8}{4}{2:^8}{4}{3:^8}{4}'.format('ind_var', 'dep_var', 'eerste', 'tweede', b))
			print(c*37)
			print('{4}{0:^8}{4}{1:^8}{4}{2:^8}{4}{3:^8}{4}'.format(ind_var[i], dep_var[i], '', '', b))
			print(c*37)
			print('{4}{0:^8}{4}{1:^8}{4}{2:^8.3g}{4}{3:^8}{4}'.format('', '', first_der[i], '', b))
		
		else:
			print(c*37)
			print('{4}{0:^8}{4}{1:^8}{4}{2:^8}{4}{3:^8.3g}{4}'.format(ind_var[i], dep_var[i], '', second_der[i-1], b))
			print(c*37)
			print('{4}{0:^8}{4}{1:^8}{4}{2:^8.3g}{4}{3:^8}{4}'.format('', '', first_der[i], '', b))
		
	


#print(first_derivative(volume, ph))
#second_derivative(volume, ph)
print(len(volume))
print(len(second_derivative(volume, ph)))
formatter(volume, ph)



    





def scale_picker(ind_var, dep_var, vertical_squares = 18, horizontal_squares = 28):
    """"Creates a scale for graph and calculates convenient increase of variable per square"""

