
# Purpose:  compute the two roots of a quadratic equation.

import math

A = float( input( "\nEnter the coefficient A: \n" ) )

B = float( input( "\nEnter the coefficient B: \n" ) )

C = float( input( "\nEnter the coefficient C: \n" ) )

print( "\nThe coefficients of the equation:\n" )
print( "  Coefficient A = ", A )
print( "  Coefficient B = ", B )
print( "  Coefficient C = ", C )


if A!=0:
    root1 = -B+math.sqrt(math.pow(B,2)-4*A*C)/2*A  
    root2 = -B-math.sqrt(math.pow(B,2)-4*A*C)/2*A
else: 
    pass


print( "\nThe roots of the equation:\n" )
print( "  Root #1 = ", round(root1,3) )  # round the result to three decimal places before printing
print( "  Root #2 = ", round(root2,3) )
