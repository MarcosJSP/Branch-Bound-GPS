# Branch-Bound-GPS
Branch &amp; Bound implementations to solve the GPS problem:
- Breadth search.
- Depth search.
- Best First.
- Subestimation (h=distance between origin and destination).



## Some outputs

```
->breadth--------------------------------------------
[A-B]
        visited nodes:16
        expanded nodes:9
        path:  [<Node B>, <Node F>, <Node S>, <Node A>]
[C-D]
        visited nodes:2
        expanded nodes:2
        path:  [<Node D>, <Node C>]
[B-M]
        visited nodes:32
        expanded nodes:17
        path:  [<Node M>, <Node D>, <Node C>, <Node P>, <Node B>]



->depth----------------------------------------------
[A-B]
        visited nodes:10
        expanded nodes:8
        path:  [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>]
[C-D]
        visited nodes:21
        expanded nodes:13
        path:  [<Node D>, <Node M>, <Node L>, <Node T>, <Node A>, <Node Z>, <Node O>, <Node S>, <Node F>, <Node B>, <Node P>,
<Node C>]
[B-M]
        visited nodes:12
        expanded nodes:8
        path:  [<Node M>, <Node D>, <Node C>, <Node P>, <Node R>, <Node S>, <Node F>, <Node B>]



->best first---------------------------------------
[A-B]
        visited nodes:24
        expanded nodes:13
        path:  [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
[C-D]
        visited nodes:2
        expanded nodes:2
        path:  [<Node D>, <Node C>]
[B-M]
        visited nodes:32
        expanded nodes:17
        path:  [<Node M>, <Node D>, <Node C>, <Node P>, <Node B>]



->subestimation------------------------------------
[A-B]
        visited nodes:6
        expanded nodes:6
        path:  [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
[C-D]
        visited nodes:2
        expanded nodes:2
        path:  [<Node D>, <Node C>]
[B-M]
        visited nodes:14
        expanded nodes:10
        path:  [<Node M>, <Node D>, <Node C>, <Node P>, <Node B>]
```

