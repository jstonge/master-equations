<script lang="ts">

	import Edges from '$components/SimpleLinks.svelte';
	import Nodes from '$components/Nodes.svelte';

	import { forceDirectedLayout } from '$lib/ForceLayout';

	// Props
	let { nodes, links, width, height, padding } = $props();

	let innerWidth = $derived(width - padding.left - padding.right);
	let innerHeight = height - padding.top;

	// Initial layout and state
	const nodes_xy = $derived(forceDirectedLayout({ 
		nodes, links, width: innerWidth, height: innerHeight, padding 
	}));
	let renderedLinks = $derived(links);
	

</script>


<svg {width} {height}>
		<g class="inner-chart">
			<Edges links={renderedLinks} nodes={nodes_xy} />
			<Nodes nodes={nodes_xy} isGroup={true}/>
		</g>
</svg>

<style>
	:global(*) {
		font-family: Inter;
		-moz-osx-font-smoothing: grayscale;
	}
</style>
