# These are two standard doors, initially closed
door1 = [1, 'closed']
door2 = [2, 'closed']

# This is a lockable door, initially closed and unlocked
ldoor1 = [1, 'closed', 'unlocked']

# This procedure opens a standard door
def open_door(door):
    door[1] = 'open'

# This procedure opens a lockable door
def open_ldoor(door):
    if door[2] == 'unlocked':
        door[1] = 'open'
