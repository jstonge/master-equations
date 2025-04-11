import type { Node, Link } from '$lib/types';
import { clone } from '$lib/utils/correlation';
import {
	forceSimulation,
	forceManyBody,
	forceLink,
	forceCollide,
	forceX,
	forceY
} from 'd3-force';

export function forceDirectedLayout({
	nodes,
	links,
	width,
	height,
	iterations = 1000
}: {
	nodes: Node[];
	links: Link[];
	width: number;
	height: number;
	iterations?: number;
}): Node[] {
	const clonedNodes = clone(nodes);
	const simulation = forceSimulation(clonedNodes)
		.force(
			'link',
			forceLink<Node, Link>(links)
				.id(d => d.id)
				.distance(100)
				.strength(0.05)
		)
		.force('charge', forceManyBody().strength(-100)) // repulsion to spread out
		.force('collision', forceCollide(18)) // space between nodes
		.force('x', forceX(width / 2).strength(0.05)) 
		.force('y', forceY(height / 2).strength(0.045)) 
		.stop();

	for (let i = 0; i < iterations; ++i) simulation.tick();

	return simulation.nodes() as Node[];
}
