import numpy as np

# Define the satisfaction function for each agent
def agent_satisfaction(price, consumption, comfort):
    return price * (1 - consumption) * comfort

# Define the cooperative game between agents
def cooperative_game(electric_system, agent_satisfactions):
    n = len(agent_satisfactions)
    # Calculate the total satisfaction of all agents
    total_satisfaction = sum(agent_satisfactions)
    # Calculate the marginal contributions of each agent
    marginal_contributions = np.zeros(n)
    for i in range(n):
        marginal_contributions[i] = (agent_satisfaction(electric_system/n, consumption[i], comfort[i]) 
                                     - agent_satisfaction(0, consumption[i], comfort[i]))
    # Allocate power using the Shapley value
    power_allocations = np.zeros(n)
    for i in range(n):
        power_allocations[i] = sum([marginal_contributions[j] for j in range(n) if j != i])/(n-1) + marginal_contributions[i]/n
    
    return power_allocations

# Example usage
# Assume the electric system needs 100 units of power
electric_system = 100

# Assume there are four agents with different satisfaction functions
price = [0.5, 0.7, 0.3, 0.6]
consumption = [0.1, 0.3, 0.2, 0.4]
comfort = [0.8, 0.5, 0.6, 0.9]

# Calculate each agent's satisfaction
agent_satisfactions = [agent_satisfaction(price[i], consumption[i], comfort[i]) for i in range(len(price))]

# Allocate power to each agent using cooperative game theory
power_allocations = cooperative_game(electric_system, agent_satisfactions)

# Print the power allocation for each agent
print("Power Allocations: ", power_allocations)

import numpy as np

# Define the tariff formulas
def calculate_tariff1(kw_demand, kwh_consumption):
    return 0.05 * kw_demand + 0.15 * kwh_consumption

def calculate_tariff2(kw_demand, kwh_consumption):
    return 0.1 * kw_demand + 0.2 * kwh_consumption

def calculate_tariff3(kw_demand, kwh_consumption):
    return 0.15 * kw_demand + 0.25 * kwh_consumption

def calculate_tariff4(kw_demand, kwh_consumption):
    return 0.2 * kw_demand + 0.3 * kwh_consumption

# Example usage
# Assume the electric system needs 100 units of power
electric_system = 100

# Assume there are five customers with different demands and consumptions
kw_demand = np.array(consumption)
kwh_consumption = np.array(power_allocations)

# Calculate the tariff for each customer using a different formula
tariff1 = calculate_tariff1(kw_demand, kwh_consumption)
tariff2 = calculate_tariff2(kw_demand, kwh_consumption)
tariff3 = calculate_tariff3(kw_demand, kwh_consumption)
tariff4 = calculate_tariff4(kw_demand, kwh_consumption)

# Print the tariff for each customer
print("Tariff 1: ", tariff1)
print("Tariff 2: ", tariff2)
print("Tariff 3: ", tariff3)
print("Tariff 4: ", tariff4)

