class VacuumCleanerAgent :
    def __init__(self):
        self.location ='A'

    def act(self, Environment):
        if Environment[self.location] == 'Dirty':
            action = 'Suck'
            Environment[self.location] = 'Clean'

        
        elif self.location == 'A':
            action = 'Right'
            self.location = 'B'

        else:
            action = 'Left'
            self.location = 'A'


        return action


environment = {'A': 'Dirty', 'B': 'Dirty'}
agent = VacuumCleanerAgent()

for i in range (6):
    action = agent.act(environment)
    print(f"Step {i+1}: Location: {agent.location}, Action: {action}, Environment: {environment}")
    if environment['A'] == 'Clean' and environment['B'] == 'Clean':
        print("Both locations are clean. Stopping the agent.")
        break 
        
