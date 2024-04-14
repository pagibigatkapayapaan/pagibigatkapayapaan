from random import choice

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'New York': 'NY',
    'California': 'CA',
    'Michigan': 'MI',
}

random_state = choice(list(states.keys()))
print(random_state)
print(states[random_state])
