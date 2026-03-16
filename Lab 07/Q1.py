def beam_Search(start, width, depth):

    states = [start]
    path = [start]

    for i in range(depth):

        new_states = []

        for s in states:
            new_states.append(s + 1)
            new_states.append(s + 2)
            new_states.append(s + 3)

        new_states.sort(reverse=True)

        states = new_states[:width]
        path.append(states[0])

    return path, states[0]

start = 0
beam_width = 2
depth = 3
moves, score = beam_Search(start, beam_width, depth)

print("Best move sequence:", moves)
print("Evaluation score:", score)
