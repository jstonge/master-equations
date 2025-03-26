<script lang="ts">
	// import { createInterval } from '$lib/utils/interval';
	import { onMount } from 'svelte';
	import type { Node, Link } from '$lib/types';
	import {
		resetNodes,
		infectNode,
		highlightNode,
        linkBetween,
		StarNode,
	} from '$lib/utils/dynamics';
	import {clone} from '$lib/utils/correlation';
	import {interpolateViridis} from 'd3-scale-chromatic';
	import { scaleLinear } from 'd3-scale';

	import { LayerCake, Svg } from 'layercake'; // Import the LayerCake and Svg components from LayerCake
	
	import Scatter from  '$components/layercake/Scatter.svelte';
	import AxisX from    '$components/layercake/AxisX.svelte';
	import AxisY from    '$components/layercake/AxisY.svelte';
	import AxisYRight from '$components/layercake/AxisYRight.svelte'; 

	import Manylinks from '$data/edges.json';

	import Edges from '$components/SimpleLinks.svelte';
	import Nodes from '$components/Nodes.svelte';

	import { radialLayout } from '$lib/RadialLayout';
	
	// Props
	let { scrollyIndex, nodes, links, width, height, padding } = $props();
    
	
	// Layout dimensions
	let innerWidth = $derived(width - padding.right);
	let innerHeight = height - padding.top - padding.bottom;
	
	// Initial layout and state
	let nodes_xy: Node[] = $state(radialLayout({ 
		nodes, links, width, height: innerHeight
	}));
	
	const mainNode = $derived(nodes_xy[0]);
	const targetNode = $derived(nodes_xy[5]);
	
	// LayerCake chart
	const xKey = 's';
	const yKeyLeft = 'MI';
	const yKeyRight = 'structuralSimilarity';
	
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

	// let renderedNodesData = $state(nodes);
	let renderedLinks = $state(links);

	let index = $state(1);
	let stopInterval: () => void = () => {};

    // Simulation parameters
    const s = 500; // contact frame duration (1000ms = 1s per frame)
    const r = 0.2; // infection rate per second
    const infectionProbPerContact = r * (s / 1000); // convert ms to seconds

	
    // State
    let contactTime = 0;
    let targetInfected = false;

    // On each step
    function takeOneStep() {
        index = (index + 1) % Manylinks.length;
        renderedLinks = Manylinks[index];

        // Check contact between source and target
        const isContact = renderedLinks.some(link => linkBetween(mainNode, targetNode, link));

        if (isContact) {
            mainNode.highlight = true;
            targetNode.highlight = true;
            contactTime += s/1e3;

            if (!targetInfected && Math.random() < infectionProbPerContact) {
                infectNode(targetNode);
                targetInfected = true;
                console.log("Infected after", contactTime, "seconds of cumulative contact.");
            }
        } else {
            mainNode.highlight = false;
            targetNode.highlight = false;
        }
    }

	function runSteps(n: number, delay: number = 1000) {
		let step = 0;

		function doStep() {
			if (step >= n) return;

			takeOneStep();
			step++;

			setTimeout(doStep, delay);
		}

		doStep();
	}
	
    $effect(() => {
		stopInterval();

        switch (scrollyIndex) {

            case 0:
                resetNodes(nodes_xy, nodes);
                
                StarNode(mainNode);
				infectNode(mainNode);
                
                StarNode(targetNode);
				highlightNode(targetNode);

				nodes_xy.forEach(n => (n.highlight = false));
				break;
            
            case 1:        
                setTimeout(() => runSteps(10, s ), 0);
                break;
        }
    })
	const colorScale = scaleLinear()
		.domain([0, 1600]) // or use extent(data[0], d => d.structuralSimilarity)
		.range([0, 1]) // domain for interpolator (0–1)
		.clamp(true);
</script>

<div class="sc-chart-container">
	<LayerCake 
	  x={yKeyRight}
	  y={yKeyLeft}
	  fill={yKeyRight}
	  data={data[0]} 
	  padding={{ top: 50, right: 50, bottom: 50, left: 50 }}
	>
	  <Svg>
		<AxisX axisTitle={yKeyRight}/>
		<AxisY axisTitle={yKeyLeft} dx={-3}/>
		<Scatter fill={(d) => interpolateViridis(colorScale(d[xKey]))} r={5} />
	  </Svg>
	</LayerCake>
</div>
<div class="chart-container" bind:clientWidth={width}>
	<svg {width} {height}>
		<g class="inner-chart" transform="translate({padding.left - 10}, {0})">
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
