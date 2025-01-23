import networkx as nx
import matplotlib.pyplot as plt

def create_weighted_city_graph():
    """Створює граф транспортної мережі міста з вагами ребер."""
    city_graph = nx.Graph()

    # Додавання вершин (станцій)
    stations = ["Station A", "Station B", "Station C", "Station D", "Station E", "Station F", "Station G"]
    city_graph.add_nodes_from(stations)

    # Додавання ребер (доріг між станціями) з вагами
    roads = [
        ("Station A", "Station B", 4),
        ("Station A", "Station C", 2),
        ("Station B", "Station D", 5),
        ("Station C", "Station D", 8),
        ("Station C", "Station E", 10),
        ("Station D", "Station F", 6),
        ("Station E", "Station F", 2),
        ("Station F", "Station G", 3),
        ("Station B", "Station G", 7)
    ]
    city_graph.add_weighted_edges_from(roads)

    return city_graph

def dijkstra_shortest_paths(graph, start_node):
    """Реалізація алгоритму Дейкстри для знаходження найкоротших шляхів."""
    # Використовуємо вбудовану функцію з бібліотеки NetworkX
    return nx.single_source_dijkstra_path_length(graph, start_node)

def visualize_graph(graph):
    """Візуалізує граф із вагами ребер."""
    pos = nx.spring_layout(graph, seed=42)
    plt.figure(figsize=(10, 8))
    nx.draw_networkx(graph, pos, with_labels=True, node_color="lightblue", node_size=1500, font_size=12)
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10)
    plt.title("Зважений граф транспортної мережі")
    plt.show()

def main():
    """Основна функція для запуску алгоритму Дейкстри."""
    # Створюємо граф
    city_graph = create_weighted_city_graph()

    # Візуалізуємо граф
    visualize_graph(city_graph)

    # Знаходимо найкоротші шляхи від кожної вершини
    for station in city_graph.nodes:
        shortest_paths = dijkstra_shortest_paths(city_graph, station)
        print(f"Найкоротші шляхи від {station}:")
        for target, distance in shortest_paths.items():
            print(f"  до {target}: {distance}")
        print()

if __name__ == "__main__":
    main()