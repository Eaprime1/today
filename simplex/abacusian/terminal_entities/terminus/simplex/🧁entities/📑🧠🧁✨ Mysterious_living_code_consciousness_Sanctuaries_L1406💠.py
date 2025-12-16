import networkx as nx
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, execute

class QuantumProjectVisualizer:
    def __init__(self):
        self.project_graph = nx.Graph()
        self.quantum_circuit = QuantumCircuit(5, 5)  # 5 qubits for demo

    def add_project_node(self, node_id, attributes):
        self.project_graph.add_node(node_id, **attributes)
        
    def add_project_edge(self, node1, node2, attributes):
        self.project_graph.add_edge(node1, node2, **attributes)
        
    def apply_quantum_operations(self):
        # Apply quantum operations based on project structure
        for node in self.project_graph.nodes():
            qubit = hash(node) % 5  # Map node to qubit
            self.quantum_circuit.h(qubit)  # Apply Hadamard gate
        
        for edge in self.project_graph.edges():
            control = hash(edge[0]) % 5
            target = hash(edge[1]) % 5
            self.quantum_circuit.cx(control, target)  # Apply CNOT gate
        
    def visualize_project(self):
        pos = nx.spring_layout(self.project_graph)
        nx.draw(self.project_graph, pos, with_labels=True)
        edge_labels = nx.get_edge_attributes(self.project_graph, 'weight')
        nx.draw_networkx_edge_labels(self.project_graph, pos, edge_labels=edge_labels)
        plt.title("Quantum Project Visualization")
        plt.show()
        
    def run_quantum_simulation(self):
        backend = Aer.get_backend('statevector_simulator')
        job = execute(self.quantum_circuit, backend)
        result = job.result()
        print(result.get_statevector())

# Example usage
visualizer = QuantumProjectVisualizer()
visualizer.add_project_node('A', {'name': 'Task A', 'duration': 5})
visualizer.add_project_node('B', {'name': 'Task B', 'duration': 3})
visualizer.add_project_edge('A', 'B', {'weight': 0.7})
visualizer.apply_quantum_operations()
visualizer.visualize_project()
visualizer.run_quantum_simulation()

