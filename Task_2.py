import networkx as nx

def create_city_graph():
    """Створює граф транспортної мережі міста."""
    city_graph = nx.Graph()

    # Додавання вершин (станцій)
    stations = ["Station A", "Station B", "Station C", "Station D", "Station E", "Station F", "Station G"]
    city_graph.add_nodes_from(stations)

    # Додавання ребер (доріг між станціями)
    roads = [
        ("Station A", "Station B"),
        ("Station A", "Station C"),
        ("Station B", "Station D"),
        ("Station C", "Station D"),
        ("Station C", "Station E"),
        ("Station D", "Station F"),
        ("Station E", "Station F"),
        ("Station F", "Station G"),
        ("Station B", "Station G")
    ]
    city_graph.add_edges_from(roads)

    return city_graph

def dfs_path(graph, start, target, visited=None, path=None):
    """Реалізація пошуку в глибину (DFS)."""
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == target:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, target, visited, path)
            if result:
                return result

    path.pop()
    return None

def bfs_path(graph, start, target):
    """Реалізація пошуку в ширину (BFS)."""
    queue = [(start, [start])]
    visited = set()

    while queue:
        current_node, path = queue.pop(0)
        visited.add(current_node)

        if current_node == target:
            return path

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited and neighbor not in [node for node, _ in queue]:
                queue.append((neighbor, path + [neighbor]))

    return None

def main():
    """Основна функція для запуску пошуку."""
    city_graph = create_city_graph()

    start = "Station A"
    target = "Station G"

    # Виконання пошуку
    dfs_result = dfs_path(city_graph, start, target)
    bfs_result = bfs_path(city_graph, start, target)

    # Виведення результатів
    print(f"Шлях DFS (глибина): {dfs_result}")
    print(f"Шлях BFS (ширина): {bfs_result}")

    # Порівняння результатів
    print("\nПояснення:")
    print("- DFS шукає шлях у глибину, тому перший знайдений шлях може бути не найкоротшим.")
    print("- BFS шукає шлях у ширину, гарантуючи найкоротший шлях у незважених графах.")

if __name__ == "__main__":
    main()