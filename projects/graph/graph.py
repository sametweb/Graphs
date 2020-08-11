"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue a starting a vertex
        q = Queue()
        q.enqueue(starting_vertex)
        # Create a set to store the visited vertices
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If vertext has not been visited
            if v not in visited:
                # Mark the vertex as visited
                visited.add(v)
                # Print it for debug
                print(v)
                # Add all of its neighbors to the back of the queue
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push a starting a vertex
        s = Stack()
        s.push(starting_vertex)
        # Create a set to store the visited vertices
        visited = set()
        # While the stack is not empty
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If vertext has not been visited
            if v not in visited:
                # Mark the vertex as visited
                visited.add(v)
                # Print it for debug
                print(v)
                # Add all of its neighbors to the top of the stack
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)


    def dft_recursive(self, starting_vertex, visited = set()):
        print(starting_vertex)
        visited.add(starting_vertex)
        if len(self.get_neighbors(starting_vertex)) > 0:
            for vertex in self.get_neighbors(starting_vertex):
                if vertex not in visited:
                    visited.add(vertex)
                    self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue "PATH To The Starting Vertex ID"
        q = Queue()
        q.enqueue([starting_vertex])

        # Create a set to store visited vertices
        visited = set()

        # While the queue is not empty
        while q.size() > 0:

            # Dequeue the first PATH
            path = q.dequeue()

            # Grab the last vertex from the PATH
            last_vertex = path[-1]

            # Check if the vertex hasn't been visited
            if last_vertex not in visited:

                # Is this vertex the target?
                if last_vertex == destination_vertex:
                    # Return the PATH
                    return path

                # Mark it as visited
                visited.add(last_vertex)

                # Then add a PATH to its neighbors to the back of the queue
                for neighbor_vertex in self.get_neighbors(last_vertex):
                # Make a copy of the PATH
                # Append the neighbor the back of the PATH
                # Enqueue out new PATH
                    q.enqueue(path + [neighbor_vertex])


        # return None
        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push "PATH To The Starting Vertex ID"
        s = Stack()
        s.push([starting_vertex])

        # Create a set to store visited vertices
        visited = set()

        # While the stack is not empty
        while s.size() > 0:

            # pop the first PATH
            path = s.pop()

            # Grab the last vertex from the PATH
            last_vertex = path[-1]

            # Check if the vertex hasn't been visited
            if last_vertex not in visited:

                # Is this vertex the target?
                if last_vertex == destination_vertex:
                    # Return the PATH
                    return path

                # Mark it as visited
                visited.add(last_vertex)

                # Then add a PATH to its neighbors to the back of the stack
                for neighbor_vertex in self.get_neighbors(last_vertex):
                # Make a copy of the PATH
                # Append the neighbor the back of the PATH
                # push out new PATH
                    s.push(path + [neighbor_vertex])


        # return None
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = set()):
        pass

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
