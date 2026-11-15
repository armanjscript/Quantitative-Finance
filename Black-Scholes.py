from scipy import stats
from numpy import log, exp, sqrt


def call_option_price(S, E, T, rf, sigma):
    #First we have to calculate d1 and d2 parameters
    d1 = (log(S/E) + (rf + sigma**2/2.0)*T) / (sigma*sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    print("The d1 and d2 parameters: %s, %s" % (d1, d2))
    
    #Use the N(x) to calculate the price of the option
    return S * stats.norm.cdf(d1) - E * exp(-rf * T) * stats.norm.cdf(d2)

 
def put_option_price(S, E, T, rf, sigma):
    #First we have to calculate d1 and d2 parameters
    d1 = (log(S/E) + (rf + sigma**2/2.0)*T) / (sigma*sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    print("The d1 and d2 parameters: %s, %s" % (d1, d2))
    
    #Use the N(x) to calculate the price of the option
    return -S * stats.norm.cdf(-d1) + E * exp(-rf * T) * stats.norm.cdf(-d2)



if __name__ == "__main__":
    
    #Underlying stock price at t=0
    S0 = 100
    
    #Strike Price
    E = 100
    
    #Expiary 1 = 1year = 365 days
    T = 1
    
    #Risk-Free rate
    rf = 0.05
    
    #Volatility of the underlying stock
    sigma = 0.2
    
    print("Call option price according to Black-Scholes model: ",
          call_option_price(S0, E, T, rf, sigma))
    print("Put option price according to Black-Scholes model: ",
          put_option_price(S0, E, T, rf, sigma))
    
    
