def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

N = 16
square_root_bisection(N)

#The square root of 16 is approximately 4.0 


#The Bisection Method is a numerical method used for solving root-finding problems. 
#It works by iteratively dividing a given interval into two halves to locate where the function f(x) equals zero (the root).
#Steps:
    #Choose an initial interval [a,b][a,b] where f(a) and f(b) have opposite signs (f(a)⋅f(b)<0).
    #Calculate the midpoint: m=(a+b)/2.
    #Evaluate f(m):
    #    If f(m)=0, then mm is the root.
    #    If f(m)⋅f(a)<0, the root lies in [a,m].
    #    Otherwise, the root lies in [m,b].
    #Repeat the process until the desired accuracy is achieved.
