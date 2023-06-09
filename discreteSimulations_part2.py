import random
import simpy
import numpy as np

NUM_EMPLOYEES = 4
AVG_SUPPORT_TIME = 5
CUSTOMER_INTERVAL = 2
SIM_TIME = 120

customers_handled = 0





class CallCenter:
    def __init__(self, env, num_employees, support_time):
        self.env = env
        self.staff = simpy.Resource(env, num_employees)
        self.support_time = support_time

    def support(self, customer):
        random_time = max(1, np.random.normal(self.support_time, 4))
        yield self.env.timeout(random_time)
        print(f"Support finished for {customer} at {self.env.now:.2f}")

def customer(env, name, call_center):
    global customers_handled
    print(f"Customer {name} enders waiting queue at {env.now:.2f}!")
    with call_center.staff.request() as request:
        yield request
        print(f"Customer {name} enders call at {env.now:.2f}")
        yield env.process(call_center.support(name))
        print(f"Customer {name} left call at {env.now:.2f}")
        customers_handled += 1

def setup(env, num_employees, support_time, customer_interval):

    call_center = CallCenter(env, num_employees, support_time)
    
    for i in range(1,6):
        env.process(customer(env, i, call_center))

    while True:
        yield env.timeout(random.randint(customer_interval - 1, customer_interval +1))
        i += 1
        env.process(customer(env, i, call_center))

    

print('Starting call center simulation')

env = simpy.Environment()
env.process(setup(env, NUM_EMPLOYEES, AVG_SUPPORT_TIME, CUSTOMER_INTERVAL))
env.run(until=SIM_TIME)


print('Customers Handled: ' + str(customers_handled))

class Vegetable:
    def __init__(self, height,spacing,seed2harvest,lb_sqrft,dollar_lb,calories_lb,):
        self.height = height # Inches
        self.spacing = spacing # #/sqrtft
        self.seed2harvest = seed2harvest # days
        self.lb_sqrft = lb_sqrft # pounds/sqrft
        self.dollar_lb = dollar_lb # dollars/pound
        self.calories_lb = calories_lb # calories/pound

# Height (in), spacing (#/ft^2), seed to harvest (days), pounds/ft^2, dollars/pound, calories/pound 
leafLettuce = Vegetable(12,4,7*7,0.75,5,68)

print(leafLettuce.height)

