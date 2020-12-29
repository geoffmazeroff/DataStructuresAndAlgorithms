import queue
from threading import current_thread

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices: return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)

    def depth_first_search(self, vertex, target, visited_vertices={}):
        # Found the target at the given vertex
        if vertex.value == target: return vertex

        visited_vertices[vertex.value] = True

        for v in vertex.adjacent_vertices:
            # Skip over veritices we've seen already
            if v.value in visited_vertices: continue

            # Found the target in the adjacent vertex
            if v.value == target: return v

            # Haven't found the target, so recursively keep searching
            target_vertex = self.depth_first_search(v, target, visited_vertices)

            # Eventually found the target, so return where it was
            if target_vertex: return target_vertex

        # Never ended up finding the target
        return None
    
    def breadth_first_search(self, starting_vertex, target):
        if starting_vertex.value == target: return starting_vertex

        q = queue.Queue()
        visited_vertices = {}
        visited_vertices[starting_vertex.value] = True
        q.put(starting_vertex)

        while not q.empty():
            current_vertex = q.get()
            
            for v in current_vertex.adjacent_vertices:
                
                if v.value == target: return v

                # Queue up any adjacent vertices we've not seen
                if v.value not in visited_vertices:
                    visited_vertices[v.value] = True
                    q.put(v)

def breadth_first_traversal(starting_vertex):
    q = queue.Queue()
    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True
    q.put(starting_vertex)

    while not q.empty():
        current_vertex = q.get()
        print(current_vertex.value)

        for v in current_vertex.adjacent_vertices:
            
            # Queue up any adjacent vertices we've not seen
            if v.value not in visited_vertices:
                visited_vertices[v.value] = True
                q.put(v)

class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_route(self, city, price):
        self.routes[city] = price

def dijkstra_shortest_path(starting_city, final_destination):
    cheapest_prices = {}
    cheapest_previous_stopover_city = {}

    unvisited_cities = []
    visited_cities = {}

    # Costs nothing to get to ourselves
    cheapest_prices[starting_city.name] = 0

    current_city = starting_city

    # Keep exploring until we've run out of cities to visit
    while current_city:
        #print("--- Processing {city} ---".format(city = current_city.name))
        # Mark this city as visited
        visited_cities[current_city.name] = True
        if current_city in unvisited_cities: unvisited_cities.remove(current_city)

        # Iterate over all adjacent cities to this one
        for city, price in current_city.routes.items():
            # Discovered a city we've not visited yet
            if city.name not in unvisited_cities: unvisited_cities.append(city)

            # Calculate the price of getting from START to ADJACENT using the
            # current city as the second-to-last stop
            price_through_current_city = price
            if current_city.name in cheapest_prices: 
                price_through_current_city += cheapest_prices[current_city.name]
                #print("  >> We've been through {city} before. Going from {p1} to {p2}.".format(city = city.name, p1 = price, p2 = price_through_current_city))
            
            # If we've never been through here or this is a cheaper price,
            # update the tables
            if (city.name not in cheapest_prices) or (price_through_current_city < cheapest_prices[city.name]):
                cheapest_prices[city.name] = price_through_current_city
                cheapest_previous_stopover_city[city.name] = current_city.name

        # DEBUG
        #print("--- Done iterating over cities adjacent to {city} ---".format(city = current_city.name))
        #for c, p in cheapest_prices.items():
        #    print("City: {city}, Price: {price}".format(city = c, price = p))
        #for c, x in cheapest_previous_stopover_city.items():
        #    print("City: {city}, Stopover: {stopover}".format(city = c, stopover = x))

        # Visit the next unvisited city. Choose the cheapest.
        min_city = None
        min_price = 999999
        for city in unvisited_cities:
            if city.name not in cheapest_prices: continue

            if cheapest_prices[city.name] < min_price:
                min_city = city
                min_price = cheapest_prices[city.name]

        current_city = min_city

    # DEBUG
    #for c, p in cheapest_prices.items():
    #    print("City: {city}, Price: {price}".format(city = c, price = p))
    #for c, x in cheapest_previous_stopover_city.items():
    #    print("City: {city}, Stopover: {stopover}".format(city = c, stopover = x))

    shortest_path = []
    current_city_name = final_destination.name

    while current_city_name != starting_city.name:
        shortest_path.append(current_city_name)
        current_city_name = cheapest_previous_stopover_city[current_city_name]

    shortest_path.append(starting_city.name)

    # Oh god, why do I need to do this???? What does shortest_path.reverse() = None????
    real_answer = []
    for x in shortest_path[::-1]:
        real_answer.append(x)
    return real_answer

# Part 1 -- set up the bidirectional graph
#            Alice
#   /       /       \        \
# Bob   Candy       Derek -- Elaine
#  |      /            |
# Fred   /           Gina
#  |    /              |
# Helen              Irena

alice = Vertex("Alice")
bob = Vertex("Bob")
candy = Vertex("Candy")
derek = Vertex("Derek")
elaine = Vertex("Elaine")
fred = Vertex("Fred")
helen = Vertex("Helen")
gina = Vertex("Gina")
irena = Vertex("Irena")
alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(candy)
alice.add_adjacent_vertex(derek)
alice.add_adjacent_vertex(elaine)
bob.add_adjacent_vertex(fred)
candy.add_adjacent_vertex(helen)
fred.add_adjacent_vertex(helen)
derek.add_adjacent_vertex(elaine)
derek.add_adjacent_vertex(gina)
gina.add_adjacent_vertex(irena)

# Part 2 -- search for things with depth-first search
print("=== Finding 'Helen' DFS...")
find_helen = alice.depth_first_search(alice, "Helen")
if find_helen: print("Found!")
else: print("Not found!")
print("=== Finding 'Geoff' DFS...")
find_helen = alice.depth_first_search(alice, "Geoff")
if find_helen: print("Found!")
else: print("Not found!")

# Part 3 -- breadth-first traversal
print("=== BFS traversal starting at 'Alice'...")
breadth_first_traversal(alice)

# Part 3a -- search for things with breadth-first search
print("=== Finding 'Helen' BFS...")
find_helen = alice.breadth_first_search(alice, "Helen")
if find_helen: print("Found!")
else: print("Not found!")
print("=== Finding 'Geoff' BFS...")
find_helen = alice.breadth_first_search(alice, "Geoff")
if find_helen: print("Found!")
else: print("Not found!")

# Part 4 -- city routes setup
print("=== Setting up routes...")
atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
elpaso = City("El Paso")
atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(elpaso, 80)
denver.add_route(chicago, 40)
denver.add_route(elpaso, 140)

# Part 5 -- cheapest route from Atlanta to El Paso
print("=== Cheapest route from Atlanta to El Paso")
print(dijkstra_shortest_path(atlanta, elpaso))