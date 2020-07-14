import requests, os                                                                 # Import the requests library 

rsi_indicator = "rsi"                                                               # Define relative strength index
fibonacci_indicator = "fibonacciretracement"                                        # Define fib retracement

rsi_endpoint = f"https://ta.taapi.io/{rsi_indicator}"                               # Define rsi endpoint 
fibonacci_endpoint = f"https://ta.taapi.io/{fibonacci_indicator}"                   # Define fib endpoint 

TAAPI_API_KEY = os.environ['TAAPI_API_KEY']                                         # fetch taapi key from environent variable

parameters = {'secret': TAAPI_API_KEY, 'exchange': 'binance', 'symbol': 'XMR/USDT', 'interval': '5m'} # Define parameters to be sent to the endpoint 

rsi_response = requests.get(url = rsi_endpoint, params = parameters)                # Send rsi get request and save the response as response object 
fibonacci_response = requests.get(url = fibonacci_endpoint, params = parameters)    # Send fib get request and save the response as response object

rsi_result = rsi_response.json()                                                    # Extract rsi data in json format 
fib_result = fibonacci_response.json()                                              # Extract fib data in json format

rsi = {'Monero/Tether Relative Strength Index [1m]': rsi_result.get('value')}       # rsi formatted indicator
fibonacci = {'Monero/Tether Fibonacci Retracement [1m]': fib_result.get('value')}   # fib formatted indicator

print(rsi)                                                                          # Print rsi indicator results
print(fibonacci)                                                                    # Print fib indicator results