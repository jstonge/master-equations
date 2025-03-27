<script>
    import { onMount } from 'svelte';
    
    import {interpolateViridis} from 'd3-scale-chromatic';
	import {scaleLinear} from 'd3-scale';
	import { LayerCake, Svg } from 'layercake'; // Import the LayerCake and Svg components from LayerCake
	

    import Scatter from  '$components/layercake/Scatter.svelte';
	import AxisX from    '$components/layercake/AxisX.svelte';
	import AxisY from    '$components/layercake/AxisY.svelte';
    
    import {clone} from '$lib/utils/correlation';

    let { nodes, nodes_xy, Manylinks, mainNode, targetNode, scrollyIndex } = $props();

    let data = $state([]);  
	let loading = true;

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
			// console.log(data[0])
		};
		
	});

    // LayerCake chart
	const xKey = 's';
	const yKeyLeft = 'MI';
	const yKeyRight = 'structuralSimilarity';
    
    const colorScale = scaleLinear()
		.domain([0, 1600]) // or use extent(data[0], d => d.structuralSimilarity)
		.range([0, 1]) // domain for interpolator (0–1)
		.clamp(true);
</script>

<div class="sc-chart-container">
	<LayerCake 
	  x={xKey}
	  y={yKeyLeft}
	  fill={yKeyRight}
	  data={data[0]} 
	  padding={{ top: 60, right: 50, bottom: 50, left: 50 }}
	>
	  <Svg>
		<AxisX axisTitle={yKeyRight}/>
		<AxisY axisTitle={yKeyLeft} dx={-3}/>
		<Scatter fill={(d) => interpolateViridis(colorScale(d[yKeyRight]))} r={5} opacity={0.6}/>
	  </Svg>
	</LayerCake>
</div>
{#if scrollyIndex > 2}
    <div class="sc-chart-container">
        <LayerCake 
        x={yKeyLeft}
        y={yKeyRight}
        fill={yKeyRight}
        data={data[0]} 
        padding={{ top: 60, right: 50, bottom: 50, left: 50 }}
        >
        <Svg>
            <AxisX axisTitle={yKeyLeft}/>
            <AxisY axisTitle={yKeyRight} dx={-3}/>
            <Scatter fill={(d) => interpolateViridis(colorScale(d[xKey]))} r={5} />
        </Svg>
        </LayerCake>
    </div>
    
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