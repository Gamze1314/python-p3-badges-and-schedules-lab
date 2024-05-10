def badge_maker(name):
    badge = f"Hello, my name is {name}."
    return badge


# takes a list of names, retunrs a list of badge messages
def batch_badge_creator(names):
    message = []
    for name in names:
        badge = f"Hello, my name is {name}."
        message.append(badge)
    return message

# room numbers 1-8v, takes a list of speakers, and assigns each speaker to a room, each room has only one speaker.
# return a new list of strings "Hello, {name}! You will be assigned to room {number}."

assigned_rooms = []
def assign_rooms(names):
      # Initialize an empty list to store the assignments
    for index, name in enumerate(names, start=1):  # Start room numbering from 1
        assigned_rooms.append(
            f"Hello, {name}! You'll be assigned to room {index}.")
    return assigned_rooms



def printer(names):
    badges = batch_badge_creator(names)
    assigned_messages = assign_rooms(names)
    for badge in badges:
        print(badge)
    for message in assigned_messages:
        print(message)

printer(["Gamze", "Celal"])