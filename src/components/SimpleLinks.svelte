<script>
    let { links } = $props()
</script>

{#each links as e}
        <g class="links">
          <line
           x1={e.source.x}
           x2={e.target.x}
           y1={e.source.y}
           y2={e.target.y}
           opacity="0.2"
           class:highlight={e.highlight === true}
           stroke-width={Math.sqrt(e.value)}
           stroke="hsla(212, 10%, 53%, 1)"
           ></line>  
        </g>
{/each}