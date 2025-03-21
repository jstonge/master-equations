<script lang="ts">    
	import Network from "$components/Network.svelte";
    import Scrolly from "$components/helpers/Scrolly.svelte";

    import nodes from "$data/nodes.csv";
    import links from "$data/edges.csv";
    
    // Global properties of the plots.
    let width = $state(400),
        height = 400;
    
    const padding = {top: 80, right: 50, bottom: 80, left: 0};
    
    let value = $state(); // Make value reactive
    
    const myNarrative = ['Original data', 'Flickering neighbors, defining who is part of the group!' ,'Back to normal', 'Changing layout']
</script>
    

<h1>Welcome master equations</h1>

<p>The following is a <a href="https://www.w3schools.com/howto/howto_css_sticky_element.asp">sticky chart</a>. As you scroll down, it'll stick to your window.</p>
<div class="chart-container-scrolly" bind:clientWidth={width}>
    <!-- Custom svelte component. -->
    <Network {value} {nodes} {links} {width} {height} {padding}/>
</div>

<section id="scrolly">
  <!-- {value || "-"} when undefined, "-", else put value -->
    <h2>Scrolly <span>{value || "-"}</span></h2>
    <div class="spacer"></div>
    <Scrolly bind:value>
        {#each myNarrative as text, i}
      <!-- This is where we change values based on a variable active. See CSS. -->
            {@const active = value === i}
            <div class="step" class:active>
          <p>{text}</p>
            </div>
        {/each}
    </Scrolly>
    <div class="spacer"></div>
</section>


We keep going after.
 
<style>
        :global(html, body) {
            margin: 0;
            background-color: #f9f9f9; /* Light background */
            text-align: center; /* Ensures all content is centered */
        }     



    /* Ensures spacing between sections */
    section,
    p {
        margin-top: 2rem; /* Adds space between elements */
        margin-bottom: 4rem; /* Adds space between elements */
    }


    .chart-container-scrolly {
        width: 40%;
        background: white;
        height: 500px;
        box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2);
        position: sticky;
        top: 15%;
        right: 5%;
        margin-left: auto;
    }


    h2 {
        position: sticky;
        top: 4em;
        margin-left: -55%;
    }

    .spacer {
        height: 75vh;
    }

    .step {
        height: 80vh;
        display: flex;
        /* Makes it a flexbox */
        place-items: center;
        /* Centers vertically */
        justify-content: center;
        /* Centers horizontally */
        margin-left: -35%;
        /* Moves it slightly to the left */
    }

    /* This is affect children p of class .step */
    .step p {
        padding: 1em;
        background: whitesmoke;
        color: #ccc;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
        transition: background 500ms ease;
        box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2);
        z-index: 10;
    }

    /* We use CSS to change properties based on 'active' state */
    .step.active p {
        background: white;
        color: black;
    }
        
</style>
    
