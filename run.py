# Search methods

import search   

ab = search.GPSProblem('A', 'B'
                       , search.romania)
cd = search.GPSProblem('C', 'D'
                       , search.romania)
bm = search.GPSProblem('B', 'M'
                       , search.romania)

print("->breadth--------------------------------------------")
print("[A-B]")
print("\tpath: ",search.breadth_first_graph_search(ab).path())
print("[C-D]")
print("\tpath: ",search.breadth_first_graph_search(cd).path())
print("[B-M]")
print("\tpath: ",search.breadth_first_graph_search(bm).path())
print("\n")

print("\n->depth----------------------------------------------")
print("[A-B]")
print("\tpath: ",search.depth_first_graph_search(ab).path())
print("[C-D]")
print("\tpath: ",search.depth_first_graph_search(cd).path())
print("[B-M]")
print("\tpath: ",search.depth_first_graph_search(bm).path())
print("\n")

print("\n->B&B---------------------------------------")
print("[A-B]")
print("\tpath: ",search.branch_Bound(ab).path())
print("[C-D]")
print("\tpath: ",search.branch_Bound(cd).path())
print("[B-M]")
print("\tpath: ",search.branch_Bound(bm).path())
print("\n")

print("\n->B&B + subestimation--------------------------------")
print("[A-B]")
print("\tpath: ",search.branch_Bound_subestimation(ab).path())
print("[C-D]")
print("\tpath: ",search.branch_Bound_subestimation(cd).path())
print("[B-M]")
print("\tpath: ",search.branch_Bound_subestimation(bm).path())
print("\n")