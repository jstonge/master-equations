<script>
    import { onMount } from 'svelte';
    
	import {group, mean} from 'd3-array';
	import { LayerCake, Svg } from 'layercake'; // Import the LayerCake and Svg components from LayerCake

    import Scatter from  '$components/layercake/Scatter.svelte';
	import AxisX from    '$components/layercake/AxisX.svelte';
	import AxisY from    '$components/layercake/AxisY.svelte';
    
    import {clone} from '$lib/utils/correlation';

    let { nodes, nodes_xy, Manylinks, mainNode, targetNode, scrollyIndex } = $props();

    let data = $state([]);  
	let averageDataS = $state([]);
	let averageDataM = $state([]);
	let selectedMetric = $state('pearsonR');

	let loading = true;

	const padding= { top: 60, right: 50, bottom: 50, left: 50 }

	onMount(() => {
		// Ensure nodes exist
		if (!mainNode || !targetNode) return;

		const worker = new Worker(new URL('$lib/utils/correlation-worker.ts', import.meta.url), {
			type: 'module'
		});

		const sValues = [1, 50, 100, 300, 500, 700, 1000, 1200, 1400];

		worker.postMessage({
			nodes: clone(nodes_xy),
			initialNodes: clone(nodes),
			manyLinks: Manylinks,
			sourceNodeId: mainNode.id,
			targetNodeId: targetNode.id,
			r: 0.2,
			sValues,
			maxSteps: 100,
			trials: 1000,
			mode: 'multi-pair-sweep'
		});

		worker.onmessage = (e) => {
			data = [e.data];
			loading = false;
			console.log(data[0]);
			averageDataS = Array.from(
				group(data[0], d => d.s), // group by 's'
				([s, entries]) => ({
					s,
					MI: mean(entries, d => d.MI),
					correlationRatio: mean(entries, d => d.correlationRatio),
					pearsonR: mean(entries, d => d.pearsonR),
					structuralSimilarity: mean(entries, d => d.structuralSimilarity)
				})
			)
			averageDataM = Array.from(
				group(data[0], d => d.structuralSimilarity), // group by 's'
				([structuralSimilarity, entries]) => ({
					structuralSimilarity,
					MI: mean(entries, d => d.MI),
					correlationRatio: mean(entries, d => d.correlationRatio),
					pearsonR: mean(entries, d => d.pearsonR)
				})
			)
		};
		
	});

</script>

{#if scrollyIndex > 1}
	<!-- Metric selector -->
	<div style="margin-bottom: 1rem;">
		<label for="metric">Y Axis:</label>
		<select id="metric" bind:value={selectedMetric} transition:fade={{ duration: 300 }}>
		<option value="MI">Mutual Information</option>
		<option value="pearsonR">Pearson Correlation</option>
		<option value="correlationRatio">Correlation Ratio</option>
		</select>
	</div>
	<div class="sc-chart-container">
		<LayerCake 
		x={"s"}
		y={selectedMetric}
		data={averageDataS} 
		padding={padding}
		>
		<Svg>
			<AxisX axisTitle={"s"}/>
			<AxisY axisTitle={selectedMetric} dx={-3}/>
			<Scatter />
		</Svg>
		</LayerCake>
	</div>
	{#if scrollyIndex > 2}
		<div class="sc-chart-container">
			<LayerCake 
			x={'structuralSimilarity'}
			y={selectedMetric}
			data={averageDataM} 
			padding={padding}
			>
			<Svg>
				<AxisX axisTitle={'structuralSimilarity'}/>
				<AxisY axisTitle={selectedMetric} dx={-3}/>
				<Scatter fill={"black"} r={5} />
			</Svg>
			</LayerCake>
		</div>
		
	{/if}
{/if}

<style>
    /*
    The wrapper div needs to have an explicit width and height in CSS.
    It can also be a flexbox child or CSS grid element.
    The point being it needs dimensions since the <LayerCake> element will expand to fill it.
    */
    .sc-chart-container {
        width: 100%;
        height: 250px;
    }
</style>