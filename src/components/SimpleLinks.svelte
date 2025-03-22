<script>
  import { fade } from 'svelte/transition';

  let { links, nodes } = $props()

  const idToX = new Map(nodes.map(d => [String(d.id), d.x]));
  const idToY = new Map(nodes.map(d => [String(d.id), d.y]));
    
  import { cubicOut } from 'svelte/easing';

  // Custom transition that fades opacity and stroke to red
  function fadeToRed(node, { duration = 400 }) {
    const style = getComputedStyle(node);
    const initialOpacity = +style.opacity || 1;

    return {
      duration,
      easing: cubicOut,
      css: t => {
        const opacity = t * initialOpacity;
        // t goes from 1 -> 0 on `out`
        // Interpolate stroke color from red to initialStroke (on `in`) or vice versa (on `out`)
        const r = Math.round(255 * (1 - t) + 106 * t); // red -> slate(106)
        const g = Math.round(0 * (1 - t) + 115 * t);
        const b = Math.round(0 * (1 - t) + 134 * t);
        const stroke = `rgb(${r},${g},${b})`;

        return `opacity: ${opacity}; stroke: ${stroke}`;
      }
    };
  }

</script>

<g class="links">
  {#each links as e}
          <line
          x1={idToX.get(e.source?.id ?? e.source)}
          x2={idToX.get(e.target?.id ?? e.target)}
          y1={idToY.get(e.source?.id ?? e.source)}
          y2={idToY.get(e.target?.id ?? e.target)}
          opacity="0.2"
          stroke-width={Math.sqrt(e.value)}
          stroke="hsla(212, 10%, 53%, 1)"
          in:fade={{ duration: 400 }}
          out:fadeToRed={{ duration: 400 }}
          ></line>  
  {/each}
</g>