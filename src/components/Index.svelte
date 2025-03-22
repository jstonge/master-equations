<script lang="ts">    
    import { getContext } from "svelte";
	import Network from "$components/Network.svelte";
    import Scrolly from "$components/helpers/Scrolly.svelte";
    import BouncingBalls from "$components/Bouncing.svelte";

    import nodes from "$data/nodes.csv";
    import Manylinks from "$data/edges.json";
    
    const copy = getContext("copy");
    
    const steps = copy.steps;

    let links = Manylinks[0]
   
    // Global properties of the plots.
    let width = $state(400),
        height = 600;
    
    const padding = {top: 50, right: 40, bottom: 100, left: 100};
    
    let value = $state(); // Make value reactive
    
    // const myNarrative = [
    //     'Annealed network. Annealed approximation let us deal directly with network ensemble. To do so, we reshuffle connections each frame of 500 millisecond, effectively drawing from network ensemble. This is the same than saying the network structure changes rapidly, with the dynamics happening at much lower rate than that of reshuffling. Why does it make sense? ', 
    //     'We freeze the network with an infected node to show the dynamics. Here we will do a SI step.',
    //     'Flickering neighbors, defining who is part of the group! Here, we limit ourselves to pairwise. Among neighbors we will select one random neighbor to maybe infect.', 
    //     "Here's the lucky neighbor. Now with some probability (50%) we infect it.", 
    //     'Success!',
    //     'Lets reset everything and move to the next thing.',
    // ]

</script>
    

<h1>Hello master equations</h1>

<div class="centered-layout">
    <div class="text-block">
        <p>This is the most quintessential example of a contagion. </p>
    </div>
    <div class="bounce-container">
        <BouncingBalls {width} {height}/>
    </div>
</div>

<p>The following is a <a href="https://www.w3schools.com/howto/howto_css_sticky_element.asp">sticky chart</a>. As you scroll down, it'll stick to your window.</p>
<div class="chart-container-scrolly" bind:clientWidth={width}>
    <Network {value} {nodes} {links} {width} {height} {padding}/>
</div>

<section id="scrolly">
    <h2>Scrolly <span>{value || "-"}</span></h2>
    <div class="spacer"></div>
    <Scrolly bind:value>
        {#each steps as text, i}
            {@const active = value === i}
            <div class="step" class:active>
                <p>{text.value}</p>
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

    h1 {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #333;
        text-transform: uppercase;
        letter-spacing: 2px;
        padding: 10px 20px;
        background: black;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        border-bottom: 3px solid #ff7e5f;
        display: inline-block;
        margin: 20px auto;
    }
            

    .centered-layout {
        display: flex;
        justify-content: center;
        align-items: center;
        max-width: 100%;
        margin: 4rem auto;
        gap: 2rem;
    }

    .text-block {
        flex: 0 1 auto;
        margin-left: auto;
        margin-right: auto;
        max-width: 400px;
        text-align: center;
    }

    .bounce-container {
        width: 300px;
        height: 300px;
        flex-shrink: 0;
        margin-right: 5%;
    }
    
    .bounce-container {
          margin-top: 10rem;
          margin-bottom: 20rem;
          width: 45%;
          height: 300px;
          margin-left: auto;
    }


    .chart-container-scrolly {
        width: 40%;
        background: white;
        height: 600px;
        box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2);
        position: sticky;
        top: 15%;
        right: 5%;
        margin-left: auto;
    }


    h2 {
        position: sticky;
        top: 4em;
        margin-left: -85%;
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
        margin-left: -45%;
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
        width: 20%;
    }

    /* We use CSS to change properties based on 'active' state */
    .step.active p {
        background: white;
        color: black;
    }
        
</style>
    
