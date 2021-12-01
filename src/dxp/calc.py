import math

def error(std: float, length: int) -> float:
    return std / length

# Compounding error
def comperror(e1: float, e2: float) -> float:
    error = math.sqrt(pow(e1, 2) + pow(e2, 2))
    return error
