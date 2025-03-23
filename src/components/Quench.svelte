<script lang="ts">
	import { createInterval } from '$lib/utils/interval';
	import {
		resetNodes,
		infectNode,
		highlightConnectedNodes,
		highlightRandomNeighbor,
		infectRandomNeighbors,
		highlightNode,
        linkBetween,
		StarNode,
		idConnectedNodes,
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
	const targetNode = $derived(nodes_xy[5]);

	// let renderedNodesData = $state(nodes);
	let renderedLinks = $state(links);

	let index = $state(1);
	let stopInterval: () => void = () => {};

    // Simulation parameters
    const s = 1; // contact frame duration (1 = 1s per frame)
    const r = 0.2; // infection rate per second
    const infectionProbPerContact = r * s;

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
            contactTime += s;

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

        switch (value) {

            case 0:
                resetNodes(nodes_xy, nodes);
                
                StarNode(mainNode);
				infectNode(mainNode);
                
                StarNode(targetNode);
				highlightNode(targetNode);

				nodes_xy.forEach(n => (n.highlight = false));
				break;
            
            case 1:        
                setTimeout(() => runSteps(50, 1000 ), 0);
                break;
                    
        }
    })

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
