#GLqG7x7y/O2AeLp+5RuA5N64KxBfB1qKpVk5aqQ/zQUrbB+ZJmEisYC3UrBh0NaaHnmh+iDW/YOq2xD4XEGCBN+gezEVoXni1CtK5VP5tycCViRtWYivQSiuExhaW3KKmfTf9120yDHNj8qkrw62HPQgvYvAqIa82mEKGQXMLflKTgykkxpb3bNj4HnO2g85yzZ8wYu7Iy7pNNxqLRxinwf41L27pkIW0Cd9gGKgFMmtmOp5XIuRXqRL7jsjqiB04FyWo7KgLB+aJ5+1XnVBClKelvLtWH1IyMhmYSXQGqM50XKcAIEJExT95fXr1WctAPwGlj+EWa+B8ayS9TLQUYyeTDOSceB5pr42e859B5jjnmTQctMF+yNgnC9jlhL7EiTUwgqtNhCIrScP

#Поиск общих участников

def find_common_participants(command_a, command_b, spliter):
    list_a = command_a.split(spliter)
    list_b = command_b.split(spliter)
    thesame = []

    for participant_a in list_a:
        for participant_b in list_b:
            if participant_a == participant_b:
                thesame += [participant_a]
    thesame.sort()
    return thesame

spliter = ","
command_a = "aboba,biba,boba,shooba,globa,gloa,gabga,labga"
command_b = "booba,shooba,abba,boba,labga,dabga,poopa,doopa"

print('Command A:')
for participant_a in command_a.split(spliter):
    print (participant_a)
print('\nCommand B:')
for participant_b in command_b.split(spliter):
    print(participant_b)

print('\nThe same participants:')
thesame=find_common_participants(command_a, command_b, spliter)
print(', '.join(thesame))
