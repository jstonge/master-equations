<!--
  @component
  Generates an SVG scatter plot. This component can also work if the x- or y-scale is ordinal, i.e. it has a `.bandwidth` method. See the [timeplot chart](https://layercake.graphics/example/Timeplot) for an example.
 -->
 <script>
    import { getContext } from 'svelte';
    import { fade } from 'svelte/transition';
  
    const { data, xGet, yGet, xScale, yScale } = getContext('LayerCake');
  
    /** @type {Number} [r=5] – The circle's radius. */
    export let r = 5;
  
    /** @type {String} [fill='#0cf'] – The circle's fill color. */
    export let fill = '#0cf';
  
    /** @type {String} [stroke='#000'] – The circle's stroke color. */
    export let stroke = '#000';
  
    /** @type {Number} [strokeWidth=0] – The circle's stroke width. */
    export let strokeWidth = 0;
    
    /** @type {Number} [opacity=1] – The circle's opacity. */
    export let opacity = 1;

    const isFunction = (f) => typeof f === 'function';
    
  </script>
  
  <g class="scatter-group">
    {#each $data as d}
      <circle
        cx={$xGet(d) + ($xScale.bandwidth ? $xScale.bandwidth() / 2 : 0)}
        cy={$yGet(d) + ($yScale.bandwidth ? $yScale.bandwidth() / 2 : 0)}
        {r}
        {opacity}
        fill={isFunction(fill) ? fill(d) : fill}
        {stroke}
        stroke-width={strokeWidth}
        transition:fade={{ duration: 300 }}
      />
    {/each}
  </g>