import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes with labels
nodes = {
    "A": "User Input",
    "B": "Preprocessing\n(Tokenization, Lemmatization, Removing Noise)",
    "C": "Intent Detection\n(TF-IDF Vectorization, Model Prediction)",
    "D": "Response Selection\n(Selecting an appropriate response)",
    "E": "User Interface\n(Displays response via Streamlit)"
}

# Add nodes to the graph
for key, label in nodes.items():
    G.add_node(key, label=label)

# Define edges (flow of the process)
edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")]

# Add edges to the graph
G.add_edges_from(edges)

# Adjust node positions for a **vertical layout**
pos = {
    "A": (0, 4),
    "B": (0, 3),
    "C": (0, 2),
    "D": (0, 1),
    "E": (0, 0)
}

# Draw the graph
plt.figure(figsize=(4, 8))  # Adjust figure size for vertical layout
labels = nx.get_node_attributes(G, 'label')  # Get node labels
nx.draw(G, pos, with_labels=True, labels=labels, node_color="lightblue",
        node_size=4000, edge_color="gray", font_size=8,
        font_weight="bold", arrows=True, verticalalignment='center')

# Set title
plt.title("Chatbot Flowchart (Vertical Layout)")

# Show the flowchart
plt.show()
