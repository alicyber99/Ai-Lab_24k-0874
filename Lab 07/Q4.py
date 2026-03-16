def beam_task_allocation(jobs, processors, beam_width):
    beams = [([0]*processors, [])]  

    for job in jobs:
        new_beams = []
        for loads, alloc in beams:
            for p in range(processors):
                new_loads = loads[:]
                new_loads[p] += job[0]  
                new_alloc = alloc[:] + [(job, p)]
                new_beams.append((new_loads, new_alloc))
        new_beams.sort(key=lambda x: max(x[0]))
        beams = new_beams[:beam_width]

    best_loads, best_alloc = beams[0]
    return best_alloc, best_loads

jobs = [(4,3),(2,5),(3,2),(7,1),(1,4)]
processors = 3
beam_width = 2

allocation, loads = beam_task_allocation(jobs, processors, beam_width)

print("Task Allocation (Job -> Processor):")
for job, p in allocation:
    print(f"Job {job} -> Processor {p}")

print("Processor Loads:", loads)
print("Max Load:", max(loads))