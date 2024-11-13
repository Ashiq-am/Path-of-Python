# create ego network
hub_ego = nx.ego_graph(G, ego)

# showing the ego network
nx.draw(hub_ego, pos, node_color="lavender",
		node_size = 800, with_labels = True)

nx.draw_networkx_nodes(
hub_ego, pos, nodelist = [ego], **options)

plt.show()
