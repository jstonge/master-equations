<script lang="ts">    
    import { getContext } from "svelte";

	import Network from "$components/Network.svelte";
	import Quench from "$components/Quench.svelte";
    import Scrolly from "$components/helpers/Scrolly.svelte";
    // import BouncingBalls from "$components/Bouncing.svelte";
    import Hero from "$components/Hero.svelte";

    import nodes from "$data/nodes.csv";
    import Manylinks from "$data/edges.json";
    
    // First entry is the original data
    let links = Manylinks[0]

    const copy = getContext("copy");    
    const steps = copy.steps;
    const postIntro = copy.postIntro;
   
    // Global properties of the plots.
    let width = $state(400),
        height = 600;
    
    const padding = {top: 50, right: 40, bottom: 100, left: 100};
    
    let scrollyIndex = $state(); // reactive scrollIndex
</script>
    

<Hero />

<section id="mean-field">
    
    <p>The following is a <a href="https://www.w3schools.com/howto/howto_css_sticky_element.asp">sticky chart</a>. As you scroll down, it'll stick to your window.</p>

    <div class="chart-container-scrolly" bind:clientWidth={width}>
        <Network {scrollyIndex} {nodes} {links} {width} {height} {padding}/>
    </div>

    <!-- <h2>Scrolly <span>{scrollyIndex || "-"}</span></h2> -->
    <div class="spacer"></div>
    <Scrolly bind:value={scrollyIndex}>
            {#each steps as text, i}
                {@const active = scrollyIndex === i}
                <div class="step" class:active>
                    <p> 
                        {@html text.value}
                    </p>
                </div>
            {/each}
    </Scrolly>
    <div class="spacer"></div>
    
</section>

<p>We keep going after. Mean-field theory is a powerful approximation, but it also has a fundamental drawback; it washes away persistent group interactions. It can somewhat ephemeral group interactions, which can be fairly inclusive as a process. For instance, many models of higher-order interactions are about paper coauthorships, where the ephemerality of the interactions is the span it takes to publish a paper. </p>

<p>But workplace and households are both great example of group behaviors that are so persistent that it influences the dynamics in ways that mean-field just cannot. If your kid get sick, the chances are that the rest of the household will get sick too. There is <em>dynamical correlation</em> between the states of individuals within the household.</p>

<section id="mean-field-versus-quench">
    
    <div class="chart-container-scrolly">
        <Quench {scrollyIndex} {nodes} {links} {width} {height} {padding}/>
    </div>

    <!-- <h2>Scrolly <span>{scrollyIndex || "-"}</span></h2> -->
    <div class="spacer"></div>
    <Scrolly bind:value={scrollyIndex}>
            {#each postIntro as text, i}
                {@const active = scrollyIndex === i}
                <div class="step" class:active>
                    <p> 
                        {@html text.value}
                    </p>
                </div>
            {/each}
    </Scrolly>
    <div class="spacer"></div>
    
</section>
 

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
        height: 550px;
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

    
    :global(.step .bold) {
        font-family: var(--sans);
    }

    @media (max-width: 1200px) {
        
        .chart-container-scrolly {
            width: 100%;
            max-width: 600px;
            margin: 2rem auto;
            position: sticky;
            top: 80px; /* adjust depending on your layout */
            z-index: 0;
            box-shadow: none;
            background: none;
        }

        .step {
            margin-left: 0;
            padding: 0 1rem;
        }

        .step p {
            width: 100%;
            max-width: 600px;
        }

        h2 {
            margin-left: 0;
        }
        }

        
</style>
    
