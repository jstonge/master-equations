<script>
    import { scaleOrdinal } from "d3-scale"


    let { nodes } = $props()
 
    let color_palette = ["#778da9", "#6a4c93", "#005f73", "#0a9396", "#94d2bd", "#e9d8a6", "#ee9b00", "#ca6702", "#bb3e03", "#ae2012", "#9b2226"]
    let color_scale = scaleOrdinal([1,2,3,4,5], color_palette)
    let isGroup = false
</script>


{#each nodes as node}
    <g class="nodes">
    <circle
        cx={node.x}
        cy={node.y}
        fill={node.infected === true ? "red" : "lightgrey"}
        stroke={node.highlight === true ? "yellow" : "black"}
        opacity=1.
        class:highlight={node.highlight === true }
        stroke-width={node.highlight === true ? 2 : 1}
        r={10}></circle>  
    </g>
    <g>
    <text
        x={node.x}
        y={node.y}
        dx={12}
        dy={4}
        font-size="12px"
        stroke="black"
        stroke-width="0.5"
    >
        <!-- {node.label[0]}. {node.label.split(" ").at(-1)} -->
        {""}
    </text>
    </g>
{/each}

<style>
    .nodes {
      filter: drop-shadow(3px 5px 2px rgb(0 0 0 / 0.4));
    }
  

    @keyframes flicker {
    0%, 100% {
        opacity: 1;
        filter: drop-shadow(0 0 6px yellow);
    }
    50% {
        opacity: 0.3;
        filter: drop-shadow(0 0 12px orange);
    }
    }

    circle.highlight {
        animation: flicker 1s ease-in-out infinite;
    }


</style>