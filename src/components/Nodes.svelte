<script>
    import { scaleOrdinal } from "d3-scale"


    let { nodes } = $props()
 
    let color_palette = ["#778da9", "#6a4c93", "#005f73", "#0a9396", "#94d2bd", "#e9d8a6", "#ee9b00", "#ca6702", "#bb3e03", "#ae2012", "#9b2226"]
    let color_scale = scaleOrdinal([1,2,3,4,5], color_palette)
    let isGroup = false

    function generateStarPath(cx, cy, outerRadius, points, innerRatio) {
        const path = [];
        const angle = Math.PI / points;

        for (let i = 0; i < 2 * points; i++) {
            const r = i % 2 === 0 ? outerRadius : outerRadius * innerRatio;
            const a = i * angle;
            const x = cx + r * Math.sin(a);
            const y = cy - r * Math.cos(a);
            path.push(i === 0 ? `M${x},${y}` : `L${x},${y}`);
        }

        path.push("Z");
        return path.join(" ");
    }
</script>

<g class="node">
{#each nodes as node}
    <g class="nodes">
    {#if node.shape === 'star'}
    <path
        d={generateStarPath(node.x, node.y, 15, 5, 0.5)} 
        fill={node.infected ? "red" : "lightgrey"}
        stroke={node.highlight ? "yellow" : "black"}
        stroke-width={node.highlight ? 2 : 1}
        class:highlight={node.highlight === true }
        opacity={1}
    />
    {:else}
    <circle
        cx={node.x}
        cy={node.y}
        fill={node.infected === true ? "red" : "lightgrey"}
        stroke={node.highlight === true ? "yellow" : "black"}
        opacity=1.
        class:highlight={node.highlight === true }
        stroke-width={node.highlight === true ? 2 : 1}
        r={10}/>
    {/if}
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
</g>

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