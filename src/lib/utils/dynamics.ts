import type { Node, Link } from '$lib/types';

export function resetNodes(nodes: Node[], initialNodes: Node[]) {
	nodes.forEach((n, i) => {
		n.infected = false;
		n.highlight = false;
		n.x = initialNodes[i].x;
		n.y = initialNodes[i].y;
	});
}

export function infectMainNode(mainNode: Node) {
	mainNode.infected = true;
}

/**
 * Return a list of neighbor node IDs connected to the given node.
 */
export function getNeighbors(links: Link[], mainId: string): string[] {
	const connectedIds = new Set<string>();

	links.forEach(link => {
		const sourceId = typeof link.source === 'object' ? link.source.id : link.source;
		const targetId = typeof link.target === 'object' ? link.target.id : link.target;

		if (sourceId === mainId && targetId !== mainId) connectedIds.add(targetId);
		else if (targetId === mainId && sourceId !== mainId) connectedIds.add(sourceId);
	});

	return Array.from(connectedIds);
}

/**
 * Highlight all neighbors of the main node (excluding itself).
 */
export function highlightConnectedNodes(nodes: Node[], links: Link[], mainId: string) {
	const neighbors = getNeighbors(links, mainId);

	nodes.forEach(n => {
		n.highlight = neighbors.includes(n.id);
	});
}

export function highlightRandomNeighbor(
	nodes: Node[],
	links: Link[],
	mainId: string
): string | null {
	const neighbors = getNeighbors(links, mainId);

	const chosenId = neighbors.length > 0
		? neighbors[Math.floor(Math.random() * neighbors.length)]
		: null;

	nodes.forEach(n => {
		n.highlight = n.id === chosenId;
	});

	return chosenId;
}
