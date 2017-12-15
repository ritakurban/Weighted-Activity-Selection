"""Create a class to define possible activities """
class activity:
    def __init__(self, name, start, finish, weight):
        self.name = name
        self.start = start
        self.finish = finish
        self.weight = weight

"""Return the end time of the activity """
def fin(activity):
    return activity.finish

"""Find the previous compatible activity using binary search. """
def search(activity, current):
    mini = 0
    maxi = current - 1
    while mini <= maxi:
        avg = (mini + maxi) // 2
        if activity[avg].finish <= activity[current].start:
            if activity[avg + 1].finish <= activity[current].start:
                mini = avg + 1
            else:
                return avg
        else:
            maxi = avg - 1
    return None

"""Return the max. weight and the sequence of activities. """
def actselectw(act):
    """Sort the activities in increasing order. """
    activity = sorted(act, key=fin)
    seq = 0
    """Find the length of the list. """
    length = len(activity)
    """Create a table of max weights. """
    table = [0 for i in range(length)]
    """Assign the first activity to the first cell of the table. """
    table[0] = activity[0].weight
    parent = [1]
    """Dynamic programming part to calculate the highest weight. """
    for i in range(1, length):
        weights = activity[i].weight
        prev = search(activity, i)
        if prev != None:
            weights += table[prev]
        if weights > table[i-1]:
            table[i] = weights
            parent.append(1)
        else:
            table[i] = table[i - 1]
            parent.append(0)

    """Find the sequence of activities. """
    seq = []
    temp = 0
    i = len(parent) - 1
    while i >= 0:
        if parent[i] == 1:
            seq.append(activity[i].name)
            temp = search(activity, i)
            i = temp
        else:
            i -= 1
    seq = seq[::-1]
    return "Max weight is " + str(table[-1]) + ". You should pick activities " + str(seq) + "."
