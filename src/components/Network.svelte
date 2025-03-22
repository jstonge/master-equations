<script lang="ts">
	import { createInterval } from '$lib/utils/interval';
	import {
		resetNodes,
		infectMainNode,
		highlightConnectedNodes,
		highlightRandomNeighbor
	} from '$lib/utils/dynamics';

	import Manylinks from '$data/edges.json';

	import Edges from '$components/SimpleLinks.svelte';
	import Nodes from '$components/Nodes.svelte';

	import { radialLayout } from '$lib/RadialLayout';

	// Props
	let { value, nodes, links, width, height, padding } = $props();

	// Layout dimensions
	let innerWidth = $derived(width - padding.right);
	let innerHeight = height - padding.top - padding.bottom;

	// Initial layout and state
	let nodes_xy: Node[] = $state(radialLayout({ nodes, links, width, height: innerHeight }));

	const mainNode = $derived(nodes_xy[0]);

	// let renderedNodesData = $state(nodes);
	let renderedLinks = $state(links);

	let index = $state(1);
	let stopInterval: () => void = () => {};

	let selectedNeighbor: string | null = null; 

	$effect(() => {
		stopInterval();

		switch (value) {
			case 0:
				resetNodes(nodes_xy, nodes);
				stopInterval = createInterval(() => {
					index = (index + 1) % Manylinks.length;
					renderedLinks = Manylinks[index];
				}, 1000);
				break;

			case 1:
				infectMainNode(mainNode);
				nodes_xy.forEach(n => (n.highlight = false));
				break;

			case 2:
				infectMainNode(mainNode);
				highlightConnectedNodes(nodes_xy, renderedLinks, mainNode.id);
				break;

			case 3:
				infectMainNode(mainNode);
				selectedNeighbor = highlightRandomNeighbor(nodes_xy, renderedLinks, mainNode.id);
				break;

			case 4:
				// infect selected neighbor with 50% probability
				if (selectedNeighbor) {
					const neighborNode = nodes_xy.find(n => n.id === selectedNeighbor);
					// if (neighborNode && Math.random() < 0.5) {
					neighborNode.infected = true;
					neighborNode.highlight = false;
					console.log(`💉 ${neighborNode.id} got infected`);
					// } else {
						// console.log(`😌 ${selectedNeighbor} resisted infection`);
					// }
				}
				break;
			case 5:
				resetNodes(nodes_xy, nodes);
		}

		return () => stopInterval();
});

$inspect(selectedNeighbor)

</script>

<div class="chart-container">
	<svg {width} {height}>
		<text
			font-size="20px"
			stroke="black"
			stroke-width="0.5"
			x={innerWidth - 20}
			y={padding.top - 10}
		>
			2019
		</text>
		<g class="inner-chart" transform="translate({padding.left - 10}, {padding.top})">
			<Edges links={renderedLinks} nodes={nodes_xy} />
			<Nodes nodes={nodes_xy} />
		</g>
	</svg>
</div>

<style>
	:global(*) {
		font-family: Inter;
		-moz-osx-font-smoothing: grayscale;
	}
</style>
