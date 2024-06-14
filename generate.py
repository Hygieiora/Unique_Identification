import random
import string


def generate_uids(num_uids):
    uids = set()
    while len(uids) < num_uids:
        uid = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
        uids.add(uid)
    return list(uids)


num_participants = 100  # Example number of participants
uids = generate_uids(num_participants)

# Print or save the generated UIDs
"""for uid in uids:
    print(uid)
"""
