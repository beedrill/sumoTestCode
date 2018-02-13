import traci
sumoCmd = ['sumo-gui', '-c', 'sumoTestCode.sumocfg']

traci.start(sumoCmd)

step = 0 
while step < 10000:
    step += 1
    traci.simulationStep()
    print traci.simulation.getArrivedIDList()

traci.stop()