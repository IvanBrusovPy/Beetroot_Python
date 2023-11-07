from typing import Dict, Optional, Tuple


class Vertex:

    def __init__(self, key: int) -> None:
        self._id = key
        self.connected_to: Dict["Vertex", int] = {}
        self.is_visited = False

    def add_neighbor(self, nbr, weight=0) -> None:
        self.connected_to[nbr] = weight

    def __str__(self) -> str:
        return f"{self._id} connected to: {[x.get_id() for x in self.connected_to]}"

    def get_connections(self) -> Tuple["Vertex"]:
        return tuple(self.connected_to.keys())

    def get_id(self) -> int:
        return self._id

    def make_visit(self):
        self.is_visited = not self.is_visited


class Graph:

    def __init__(self) -> None:
        self.vertices_dict: Dict[int, Vertex] = {}
        self.num_vertices: int = 0
        self.visit_color = False

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices_dict[key] = new_vertex
        return new_vertex

    def get_vertex(self, n: int) -> Optional[Vertex]:
        if n in self.vertices_dict:
            return self.vertices_dict[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices_dict

    def add_edge(self, f, t, weight=0) -> None:
        if f not in self.vertices_dict:
            self.add_vertex(f)
        if t not in self.vertices_dict:
            self.add_vertex(t)
        self.vertices_dict[f].add_neighbor(self.vertices_dict[t], weight)

    def get_vertices(self) -> tuple:
        return tuple(self.vertices_dict.keys())

    def __iter__(self):
        return iter(self.vertices_dict.values())

    def deep_first_print(self):
        def print_connections(vertex: Vertex):  # Task 1
            if vertex.is_visited is self.visit_color:
                print(vertex.get_id(), "->", end=" ")
                vertex.make_visit()
                if len(vertex.connected_to) != 0:
                    for i in vertex.connected_to:
                        print_connections(i)

        start_vertex = self.vertices_dict[0]
        print_connections(start_vertex)
        self.visit_color = not self.visit_color
        print("\n")

    def breadth_first_search(self, start_vertex: int, end_vertex: int):  # Task2
        visited = []

        if (self.get_vertex(start_vertex) and self.get_vertex(end_vertex)
                and start_vertex != end_vertex):

            start = self.get_vertex(start_vertex)
            visited.append(start)
            while len(visited) != len(self.vertices_dict.values()):
                for i in visited:
                    for j in i.connected_to.keys():
                        if j not in visited:
                            print(j.get_id(), '->')
                            visited.append(j)

            # print("No way to vertex")

        else:
            raise ValueError("No such vertex in graph")
        self.visit_color = not self.visit_color
