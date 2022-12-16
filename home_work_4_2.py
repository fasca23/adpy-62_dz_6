
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def unique_ids(ids):
       return set(sum(ids.values(), []))

assert unique_ids(ids=ids) == {98, 35, 15, 213, 54, 119}