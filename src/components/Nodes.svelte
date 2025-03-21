<script>
    let { nodes, color_scale } = $props()
</script>


{#each nodes as node}
    <g class="nodes">
    <circle
        cx={node.x}
        cy={node.y}
        fill={color_scale(node.group)}
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
        {node.label[0]}. {node.label.split(" ").at(-1)}
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


    @keyframes flickerLink {
    0%, 100% {
        stroke: yellow;
        opacity: 1;
    }
    50% {
        stroke: orange;
        opacity: 0.2;
    }
    }

    line.highlight {
    animation: flickerLink 1s ease-in-out infinite;
    stroke-width: 3;
    }
</style>