import heapq
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx

INF = math.inf

COST = [
    [INF,  10,   8,   9],
    [ 10, INF,   5,   7],
    [  8,   5, INF,   6],
    [  9,   7,   6, INF],
]

N = len(COST)


def reduce_matrix(matrix):
    mat = [row[:] for row in matrix]
    cost = 0
    for i in range(N):
        row_min = min(mat[i])
        if row_min != INF and row_min > 0:
            cost += row_min
            mat[i] = [v - row_min if v != INF else INF for v in mat[i]]
    for j in range(N):
        col_min = min(mat[i][j] for i in range(N))
        if col_min != INF and col_min > 0:
            cost += col_min
            for i in range(N):
                if mat[i][j] != INF:
                    mat[i][j] -= col_min
    return mat, cost


def tsp_branch_and_bound():
    root_matrix, root_bound = reduce_matrix(COST)
    pq = [(root_bound, 0, 0, [0], root_matrix)]
    best_cost = INF
    best_path = []

    # Tree tracking: (parent_label, child_label, edge_label, pruned)
    tree_edges = []
    node_bounds = {"C0\nBound=25": 25}
    root_label = "C0\nBound=25"

    print("TSP Branch and Bound")
    print("=" * 40)
    print("Cost Matrix:")
    header = "       " + "  ".join(f"C{j}" for j in range(N))
    print(header)
    for i, row in enumerate(COST):
        vals = "  ".join("INF" if v == INF else f"{v:3}" for v in row)
        print(f"  C{i}  {vals}")
    print()

    nodes_explored = 0

    while pq:
        bound, level, current, path, matrix = heapq.heappop(pq)

        parent_label = "→".join(f"C{c}" for c in path) + f"\nBound={bound:.0f}"

        if bound >= best_cost:
            print(f"  Pruned: path={path}, bound={bound:.0f} >= best={best_cost:.0f}")
            continue

        nodes_explored += 1

        if level == N - 1:
            tour_cost = bound + (matrix[current][0] if matrix[current][0] != INF else 0)
            full_path = path + [0]
            child_label = "→".join(f"C{c}" for c in full_path) + f"\nCost={tour_cost:.0f}"
            tree_edges.append((parent_label, child_label, f"→C0", False, True))
            node_bounds[child_label] = tour_cost
            print(f"  Complete tour: {full_path}, cost={tour_cost:.0f}")
            if tour_cost < best_cost:
                best_cost = tour_cost
                best_path = full_path
            continue

        for j in range(N):
            if j in path:
                continue

            child_mat = [row[:] for row in matrix]
            child_mat[current] = [INF] * N
            for i in range(N):
                child_mat[i][j] = INF
            child_mat[j][0] = INF

            child_mat, reduction = reduce_matrix(child_mat)
            edge_cost = matrix[current][j] if matrix[current][j] != INF else INF
            if edge_cost == INF:
                continue

            child_bound = bound + edge_cost + reduction
            child_path = path + [j]
            child_label = "→".join(f"C{c}" for c in child_path) + f"\nBound={child_bound:.0f}"
            node_bounds[child_label] = child_bound

            pruned = child_bound >= best_cost
            tree_edges.append((parent_label, child_label, f"→C{j}", pruned, False))

            print(f"  Exploring: path={child_path}, bound={child_bound:.0f}")
            if not pruned:
                heapq.heappush(pq, (child_bound, level + 1, j, child_path, child_mat))

    print()
    print("=" * 40)
    print(f"Optimal Path : {' -> '.join(f'City{c}' for c in best_path)}")
    print(f"Minimum Cost : {best_cost:.0f}")
    print(f"Nodes Explored: {nodes_explored}")

    return tree_edges, node_bounds, best_path, best_cost


def draw_tree(tree_edges, node_bounds, best_path, best_cost):
    G = nx.DiGraph()
    edge_colors = {}
    optimal_label = "→".join(f"C{c}" for c in best_path) + f"\nCost={best_cost:.0f}"

    for parent, child, elabel, pruned, complete in tree_edges:
        G.add_edge(parent, child, label=elabel)
        edge_colors[(parent, child)] = ("red" if pruned else ("green" if complete else "#555555"))

    # Hierarchical layout by level
    levels = {}
    for node in G.nodes():
        lvl = node.count("→")
        levels.setdefault(lvl, []).append(node)

    pos = {}
    for lvl, nodes in levels.items():
        for i, node in enumerate(nodes):
            x = (i - (len(nodes) - 1) / 2) * 3.5
            pos[node] = (x, -lvl * 2.2)

    fig, ax = plt.subplots(figsize=(18, 10))
    ax.set_facecolor("#f9f9f9")
    fig.patch.set_facecolor("#f9f9f9")

    node_color_list = []
    for node in G.nodes():
        if node == optimal_label:
            node_color_list.append("#2ecc71")
        elif "Pruned" in node or node_bounds.get(node, 0) >= best_cost and "Cost" not in node:
            node_color_list.append("#e74c3c")
        else:
            node_color_list.append("#3498db")

    # Recolor pruned nodes
    pruned_nodes = set(child for _, child, _, pruned, _ in tree_edges if pruned)
    node_color_list = []
    for node in G.nodes():
        if node == optimal_label:
            node_color_list.append("#2ecc71")
        elif node in pruned_nodes:
            node_color_list.append("#e74c3c")
        else:
            node_color_list.append("#3498db")

    ec_list = [edge_colors.get((u, v), "#555555") for u, v in G.edges()]

    nx.draw_networkx_nodes(G, pos, node_color=node_color_list, node_size=2200, ax=ax, alpha=0.92)
    nx.draw_networkx_labels(G, pos, font_size=7, font_color="white", font_weight="bold", ax=ax)
    nx.draw_networkx_edges(G, pos, edge_color=ec_list, arrows=True,
                           arrowsize=18, width=2, ax=ax,
                           connectionstyle="arc3,rad=0.05")
    edge_labels = {(u, v): d["label"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7, ax=ax)

    ax.set_title("TSP Branch and Bound Search Tree – 4 Cities\nOptimal: " +
                 " → ".join(f"City{c}" for c in best_path) + f"  |  Min Cost = {best_cost:.0f}",
                 fontsize=13, fontweight="bold", pad=15)

    legend = [
        mpatches.Patch(color="#3498db", label="Explored Node"),
        mpatches.Patch(color="#2ecc71", label="Optimal Tour"),
        mpatches.Patch(color="#e74c3c", label="Pruned Branch"),
    ]
    ax.legend(handles=legend, loc="lower right", fontsize=9)
    ax.axis("off")

    out = "Visualization.png"
    plt.tight_layout()
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\nVisualization saved as {out}")


if __name__ == "__main__":
    tree_edges, node_bounds, best_path, best_cost = tsp_branch_and_bound()
    draw_tree(tree_edges, node_bounds, best_path, best_cost)
