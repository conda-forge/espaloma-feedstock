import torch
import espaloma

from openff.toolkit import Molecule



graph = espaloma.Graph(Molecule.from_smiles("CN1C=NC2=C1C(=O)N(C(=O)N2C)C"))

model = espaloma.get_model("latest")

model(graph.heterograph)

espaloma.graphs.deploy.openmm_system_from_graph(graph)
