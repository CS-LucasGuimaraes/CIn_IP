"""
==============================
GLOBAL VARIABLES AND CONSTANTS
==============================
"""

# Constant that simulates x -> 0 (infinite low values).
h = float(1e-9)


def find_root(x1,y1, a,b,c,d,e):
    """
    Finds the root of the function f(x) using the Newton-Raphson method.

    Args:
      x1 (int): The actual guess for the root.
      y1 (int): The value of f(x1).
      a, b, c, d, e (int): Coefficients of the function f(x) = a(x+b)^c + (ex) + d

    Returns:
      bool: True if the root was found, False otherwise.
    """

    global h

    # Compute the derivative of f(x) at x1
    derivate =  ( ((a*((x1+h)+b)**c)+(e*(x1+h))+d) - ((a*(x1+b)**c)+(e*x1)+d) ) / h

    # If the derivative is zero, the function is tangent to the x-axis and there is no root
    if (derivate == 0):

        # The fuction is a constant function with indepedent term equals to y1.
        equation = f"y={y1}"
      
        print(f"Encontramos o ponto ({round(x1, 3)};{round(y1, 3)}) da função, a equação da reta tangente deste ponto é aproximadamente {equation}, porém, ainda não é a raiz devemos continuar para otimizar a trajetória do disparo.")
      
        print(f"Droga, a reta tangente {equation} é paralela ao eixo das abscissas, não tem raiz, tenho pena de quem estiver usando a arma quando isto acontecer, kkkkk.")

        return False
    
    # Compute the independent term of the tangent line using the derivate of f(x) at x1.
    independent_term = y1-(derivate*x1)

    # Compute if a + signal is necessary while formating the equation.
    signal = '+' if independent_term >= 0 else ''

    # Build the tangent line in the form ax+b, using a=derivate and b=indepent_term.
    equation = f"y={round(derivate,3)}*x{signal}{round(independent_term,3)}"

    
    print(f"Encontramos o ponto ({round(x1, 3)};{round(y1, 3)}) da função, a equação da reta tangente deste ponto é aproximadamente {equation}, porém, ainda não é a raiz devemos continuar para otimizar a trajetória do disparo.")


    # Computes the new guess (the next aproximation of the root) and its f(x).
    x2 = (-independent_term)/derivate
    y2 = (a*(x2+b)**c)+(e*x2)+d


    # If the y-value of the next approximation is close to zero, we have found the root
    if -0.0009 < y2 and y2 < 0.0009: 
        print(f"Acertou em cheio! A raiz foi encontrada e o valor dela nas abscissas é aproximadamente {round(x2, 3)}, e a equação da reta tangente neste ponto é aproximadamente {equation}.")
        return True
    
    # Otherwise, continue iterating
    else:
        return find_root(x2,y2, a,b,c,d,e)


def main():
    """
    Reads the coefficients of the function f(x) and calls the find_root() function to find the root.
    """

    x1 = float(input())

    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())

    y1 = (a*(x1+b)**c)+(e*x1)+d

    # Check if the function is a horizontal line
    if a == 0 and e*x1 == 0:
        print(f"Maldição, a função é aproximadamente a reta y={d} que é paralela ao eixo das abscissas, não tem raiz e não é possível aplicar o método.")

    else:
        find_root(x1,y1, a,b,c,d,e)

    return 1


main()  # Start the program execution
