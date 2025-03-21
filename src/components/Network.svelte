<script>
    
    import { scaleOrdinal } from "d3-scale"
    
    import Edges from "$components/SimpleLinks.svelte";
    import Nodes from "$components/Nodes.svelte";

    import { forceDirectedLayout } from "./ForceLayout.js";
    import { radialLayout } from "./RadialLayout.js";
    
    let { value, width, height, nodes, links, padding } = $props();

    let innerWidth = $derived(width - padding.right);
    let innerHeight = height - padding.top - padding.bottom;

    let color_palette = ["#778da9", "#6a4c93", "#005f73", "#0a9396", "#94d2bd", "#e9d8a6", "#ee9b00", "#ca6702", "#bb3e03", "#ae2012", "#9b2226"]
    let color_scale = scaleOrdinal([1,2,3,4,5], color_palette)

    // Make data reactive
    let initialData = nodes;
    let renderedData = $state(initialData);

    let nodes_xy = $state(radialLayout({ 
        nodes, links, width, height: innerHeight 
    }));
    

    $effect(() => {
        if (value == 0) {
            renderedData = initialData;
            nodes_xy.forEach(n => n.highlight = false);
            links.forEach(l => l.highlight = false);

        } else if (value == 1) {
           // Step 1: Pick the main node (e.g. first one)
            const mainNode = nodes_xy[0];
            mainNode.highlight = true;

            // Step 2: Find connected nodes and highlight them
            const connectedNodeIds = new Set();

            links.forEach(link => {
            const sourceId = typeof link.source === 'object' ? link.source.id : link.source;
            const targetId = typeof link.target === 'object' ? link.target.id : link.target;

            if (sourceId === mainNode.id) {
                connectedNodeIds.add(targetId);
                link.highlight = true;
            } else if (targetId === mainNode.id) {
                connectedNodeIds.add(sourceId);
                link.highlight = true;
            }
            });

            // Step 3: Highlight connected nodes
            nodes_xy.forEach(n => {
            if (connectedNodeIds.has(n.id)) {
                n.highlight = true;
            }
            });

        } else if (value == 2) {
            renderedData = initialData;
            nodes_xy.forEach(n => n.highlight = false);
            links.forEach(l => l.highlight = false); 
        } else if (value == 3) {
            nodes_xy = forceDirectedLayout({ 
                nodes, links, width, height: innerHeight 
            });
        }  
     });

</script>

<div class="chart-container">
    <svg {width} {height}>
        <text font-size="20px" stroke="black" stroke-width="0.5" x={innerWidth-20} y={padding.top-10}>2019</text>
        <g class="inner-chart" transform="translate({padding.left-10}, {padding.top})">
            <Edges {links} />
            <Nodes nodes={nodes_xy} color_scale={color_scale} />
    </svg>
</div>

<style>

  
    :global(*) {
      font-family: Inter;
      -moz-osx-font-smoothing: grayscale;
}  
</style>