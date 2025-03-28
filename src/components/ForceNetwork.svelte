<script lang="ts">

	import Edges from '$components/SimpleLinks.svelte';
	import Nodes from '$components/Nodes.svelte';

	import { forceDirectedLayout } from '$lib/ForceLayout';

	// Props
	let { nodes, links, width, height, padding } = $props();

	// Initial layout and state
	const nodes_xy = forceDirectedLayout({ nodes, links, width, height, padding });
	let renderedLinks = $state(links);


</script>


<div class="chart-container">
	<svg {width} {height}>
		<g class="inner-chart">
			<Edges links={renderedLinks} nodes={nodes_xy} />
			<Nodes nodes={nodes_xy} isGroup={true}/>
		</g>
	</svg>
</div>

<style>
	:global(*) {
		font-family: Inter;
		-moz-osx-font-smoothing: grayscale;
	}
	
</style>
