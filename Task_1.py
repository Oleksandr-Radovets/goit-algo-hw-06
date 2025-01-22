import networkx as nx
import matplotlib.pyplot as plt

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

def analyze_and_visualize_graph(graph):
    """Аналізує та візуалізує заданий граф."""
    # Візуалізація графа
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(graph, seed=42)  # Розташування вершин
    nx.draw_networkx(graph, pos, with_labels=True, node_color="skyblue", node_size=1500, font_size=12, edge_color="gray")
    plt.title("Транспортна мережа міста")
    plt.show()

    # Аналіз основних характеристик графа
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    degrees = dict(graph.degree())

    print(f"Кількість вершин: {num_nodes}")
    print(f"Кількість ребер: {num_edges}")
    print("Ступінь вершин:")
    for station, degree in degrees.items():
        print(f"  {station}: {degree}")

def main():
    """Основна функція для створення та аналізу графа."""
    city_graph = create_city_graph()
    analyze_and_visualize_graph(city_graph)

if __name__ == "__main__":
    main()