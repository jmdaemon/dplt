import math

def average(vals: list) -> float:
    return (sum(vals) / len(vals))

def std_dev(vals: list) -> float:
    mean = average(vals)
    var = sum(pow(val - mean, 2) for val in vals) / len(vals)
    std = math.sqrt(var)
    # return std, mean, var
    return std

def error(vals: list) -> float:
    std, _, _ = std_dev(vals)
    return std / len(vals)

# No std_dev calc
def errorf(std: float, length: int) -> float:
    return std / length

# Compounding error
def comperror(e1: float, e2: float) -> float:
    error = math.sqrt(pow(e1, 2) + pow(e2, 2))
    return error

def force(mass: float, acc: float) -> float:
    return (mass * acc)
