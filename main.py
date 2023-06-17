print("Hello!, welcome to the program")

a = float(input("Enter the coefficient of x² : "))
b = float(input("Enter the coefficient of x : "))
c = float(input("Enter the constant term : "))

if(a == 0):
    print("Then this can't be a quadratic polynomial !")

#Finding the discriminant of the given quadratic equation
discriminant = ((b**2) - (4*a*c))

#Finding the two possible roots
alpha = (-b + (((b**2)-(4*a*c))**0.5)) / (2*a)
beta = (-b - (((b**2)-(4*a*c))**0.5 )) / (2*a)

#Displaying the roots
if (discriminant == 0):
    print("The roots are real and equal")

    print("The value of alpha is : ", alpha)
    print("The value of beta is : ", beta)

elif (discriminant > 0):
    print("The roots are real and unique")

    print("The value of alpha is : ", alpha)
    print("The value of beta is : ", beta)

elif (discriminant < 0):
    print("The roots are imaginary")