#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:12:18 2019

@author: vivek
"""


#Checks isomorphism of two graphs
# graph_iso.py

from networkx import Graph
from isomorph import is_isomorphic


def graph_input(g):
    nodes = [x for x in input("Enter nodes to add to graph: ").split()]
    g.add_nodes_from(list(set(nodes)))

    print("Enter end vertices of edges of graph:")
    edges = []

    while True:
        edge = tuple(input().split())
        if not edge:
            break
        edges.append(edge)

    edges = tuple(set(edges))
    g.add_edges_from(edges)


G1 = Graph()
G2 = Graph()

graph_input(G1)
graph_input(G2)

print("Graphs are isomorphic:", is_isomorphic(G1, G2))

print('In new branch')

