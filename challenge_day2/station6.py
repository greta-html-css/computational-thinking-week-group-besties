from tests import tests

def solution_station_6(numbers):
    # def sin_taylor(x):
        # pi = 3.141592653589793
        # while x > 2 * pi:
            # x -= 2 * pi
        # while x < -2 * pi:
            # x += 2 * pi
        
        # result = 0
        # term = x
        # n = 1
        # for i in range(15):
            # result += term
            # term *= -x * x / (n * (n + 1))
            # n += 2
        
        # return result

    def sin_taylor(x):
        pi = 3.141592653589793
        while x > 2 * pi:
            x -= 2 * pi
        while x < -2 * pi:
            x += 2 * pi

        result = 0
        term = x
    
        for i in range(1, 16): 
            result += term
            term *= -x * x / ((2 * i) * (2 * i + 1))
        
        return result

    
    results = []
    for num in numbers:
        results.append(sin_taylor(num))
    return results

#sample input, sample output, input
#2.2, 52, 0.8085
#0.3, 21, 0.2955
#1.4, 66, 0.9854
#1.6, 12, 0.996
#0.7, 45, 0.6442
