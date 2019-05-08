# Search methods

import search   

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("->breadth")
print(search.breadth_first_graph_search(ab).path())

print("\n->depth")
print(search.depth_first_graph_search(ab).path())

print("\n->best first")
print(search.branch_Bound_best_first(ab).path())

print("\n->subestimation")
print(search.branch_Bound_subestimation(ab).path())
