# A-Star
A star算法总结(Summary of the A star Method)


### a.将开始点记录为当前点P
### b.将当前点P放入封闭列表
### c.搜寻点P所有邻近点，假如某邻近点既没有在开放列表或封闭列表里面，则计算出该邻近点的F值，并设父节点为P，然后将其放入开放列表
### d.判断开放列表是否已经空了，如果没有说明在达到结束点前已经找完了所有可能的路径点，寻路失败，算法结束；否则继续。
### e.从开放列表拿出一个F值最小的点，作为寻路路径的下一步。
### f.判断该点是否为结束点，如果是，则寻路成功，算法结束；否则继续。
### g.将该点设为当前点P，跳回步骤c。

'''

    function reconstruct_path(cameFrom, current)
    total_path := {current}
    while current in cameFrom.Keys:
        current := cameFro
        [current]
        total_path.append(current)

    return total_path
    function A_Star(start, goal)

    // The set of nodes already evaluated
    closedSet := {}

    // The set of currently discovered nodes that are not evaluated yet.

    // Initially, only the start node is known.
    openSet := {start}

    // For each node, which node it can most efficiently be reached from.
    // If a node can be reached from many nodes, cameFrom will eventually contain the
    // most efficient previous step.
    cameFrom := an empty map

    // For each node, the cost of getting from the start node to that node.
    gScore := map with default value of Infinity

    // The cost of going from start to start is zero.
    gScore[start] := 0

    // For each node, the total cost of getting from the start node to the goal
    // by passing by that node. That value is partly known, partly heuristic.
    fScore := map with default value of Infinity

    // For the first node, that value is completely heuristic.
    fScore[start] := heuristic_cost_estimate(start, goal)

    while openSet is not empty
        current := the node in openSet having the lowest fScore[] value
        if current = goal
            return reconstruct_path(cameFrom, current)

        openSet.Remove(current)
        closedSet.Add(current)

        for each neighbor of current
            if neighbor in closedSet
                continue		// Ignore the neighbor which is already evaluated.

            // The distance from start to a neighbor
            tentative_gScore := gScore[current] + dist_between(current, neighbor)

            if neighbor not in openSet	// Discover a new node
                openSet.Add(neighbor)
            else if tentative_gScore >= gScore[neighbor]
                continue		// This is not a better path.

            // This path is the best until now. Record it!
            cameFrom[neighbor] := current
            gScore[neighbor] := tentative_gScore
            fScore[neighbor] := gScore[neighbor] + heuristic_cost_estimate(neighbor, goal)
'''