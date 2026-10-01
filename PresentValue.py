import math

def future_value_discrete(pv, r, n):
    return pv * (1 + r) ** n


def present_value_discrete(fv, r, n):
    return fv / (1 + r) ** n


def future_value_continous(pv, r, t):
    return pv * math.exp(r*t)


def present_value_continous(fv, r, t):
    return fv * math.exp(-r*t)


result = future_value_discrete(1000, 0.06, 2)

print(f"Future Value of Money (Discrete): ${result:.2f}")


result = present_value_discrete(1000, 0.06, 2)

print(f"Present Value of Money (Discrete): ${result:.2f}")


#Contionous

result = future_value_continous(1000, 0.06, 2)

print(f"Future Value of Money (Contionous): ${result:.2f}")


result = present_value_continous(1000, 0.06, 2)

print(f"Present Value of Money (Contionous): ${result:.2f}")


