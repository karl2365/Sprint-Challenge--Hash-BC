#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve
                        )


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []

    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    destination = hash_table_retrieve(hashtable, 'NONE')

    while destination != 'NONE':
        route.append(destination)
        destination = hash_table_retrieve(hashtable, destination)

    return route
