<script lang="ts">
	import { getContext } from 'svelte';
	import { innerWidth } from 'svelte/reactivity/window';
	import Network from '$components/Network.svelte';
	import Quench from '$components/Quench.svelte';
	import ForceNetwork from '$components/ForceNetwork.svelte';
	import Scrolly from '$components/helpers/Scrolly.svelte';
	import Hero from '$components/Hero.svelte';

	import nodes from '$data/nodes.csv';
	import nodes_all from '$data/nodelist_all.csv';
	import Manylinks from '$data/edges.json';
	import links_all from '$data/edgelist_all.csv';

	let links = Manylinks[0];
	const copy = getContext("copy");
	const steps = copy.steps;
	const postIntro = copy.postIntro;

	let width = $state(innerWidth.current > 1200 ? 500 : 350);
	let height = 600;
	const padding = { top: 20, right: 40, bottom: 20, left: 60 };
	let scrollyIndex = $state();
</script>

<Hero />

<section id="mean-field">
    <h2>Part I: Annealing</h2>
    <p>But doing math on exact networks can get… messy. It’s often unwieldy to carry full structure through the equations. So instead, people often model the average effect of the dynamics — smoothing over the specific network in favor of general trends.</p>
    <p>To preserve some notion of structure without going fully detailed, modelers sometimes use what’s called an <u>annealed approximation</u>.</p>
    <p>Borrowed from metallurgy, annealing refers to the process of slowly cooling a metal so that its atomic structure settles into a stable — though not static — configuration. In network modeling, annealed networks refer to a similar idea: connections between nodes are not fixed, but constantly reshuffling, like social ties in a fast-moving crowd. <p>But why does that make sense? Think back to the bouncing balls. On average, the more infected balls there were, the more likely you were to bump into one. That’s the essence of a <u>mean-field approximation</u> — we ignore the specific bump and just look at average exposure.</p>

    <div class="chart-container-scrolly" >
        <Network {scrollyIndex} {nodes} {links} {width} {height} {padding} isRadial={true}/>
    </div>

    <div class="spacer"></div>
    <Scrolly bind:value={scrollyIndex}  offset={innerWidth.current > 1200 ? '50vh' : '20vh'}>
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


<section id="mean-field-versus-quench">
    <h2>Part II: Quenching</h2>
    <p>The annealed assumption is a powerful one, but it also has a fundamental drawback; it washes away persistent group interactions. In that sense, this is terrible (but still slightly better than the bouncing ball world). It can somewhat ephemeral group interactions, which can be fairly inclusive as a process. For instance, many models of <u>higher-order interactions</u> (or complex contagion) are about paper coauthorships, where the ephemerality of the interactions is the span it takes to publish a paper. It might be good enough.</p>
    <p>But workplace and households are both great example of group behaviors that are so persistent that it influences the dynamics in ways that mean-field just cannot. If your kid get sick, the chances are that the rest of the household will get sick too. There is <em>dynamical correlation</em> between the states of individuals within the household.</p>
    
    <div class="chart-container-scrolly">
        <Quench {scrollyIndex} {nodes} {links} {width} {height} {padding}/>
    </div>

    <div class="spacer"></div>
    <Scrolly bind:value={scrollyIndex}  offset={innerWidth.current > 1200 ? '50vh' : '20vh'}>
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
 
<section class="bonus">
<p>This is it, now you should have a better idea what physicists mean when they say that annealed networks are thought to be reshuffled constantly, leading to the system the relax faster than the dynamics. In contrast, quench changes slowly compared to the dynamics, meaning that local structures can strongly influence the dynamics.</p>

<h3>Bonus content</h3>
    <p>For your information, the network we've been using is that of the coauthorship at the Vermont Complex System Institute (VCSI) for the year 2019. More precisely, the projection of the coauthorship networks whereas people share papers.</p>

    
    <div class="chart-container">
        <ForceNetwork {nodes} {links} {width} height={500} {padding}/>
    </div>

    <p>The projection is kinda dumb; is two people have been one the same paper, we simply draw an edge between them. Sure, the weight help see which coauthors are coauthoring more often together, but it means we end up with a lot of perhaps superfluous links. What does the raw data looks like? (WIP)</p>
    
    <!-- <div class="full-chart-container">
        <ForceNetwork nodes={nodes_all} links={links_all} {width} height={800} {padding}/>
    </div> -->
</section>


<style>
	:global(html, body) {
		margin: 0;
		background-color: whitesmoke;
		font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
	}

	section,
	h2,
	h3,
	p {
		color: #1a1a1a;
		text-align: left;
		margin: 2rem 10rem;
	}

	section h2 {
		font-size: 36px;
	}

	section p {
		font-size: 22px;
	}

	.chart-container-scrolly {
		width: 40%;
		height: 550px;
		position: sticky;
		top: calc(50vh - 275px);
		right: 5%;
		margin-left: auto;
	}

	.chart-container {
		width: fit-content;
		margin: 0 auto;
		display: block;
	}

	.spacer {
		height: 75vh;
	}

	.step {
		height: 80vh;
		display: flex;
		place-items: center;
		justify-content: center;
	}

	.step p {
		padding: 0.5rem 1rem;
		background: whitesmoke;
		color: #ccc;
		border-radius: 5px;
		display: flex;
		flex-direction: column;
		justify-content: center;
		transition: background 500ms ease;
		box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2);
		z-index: 10;
		width: 40%;
		transform: translateX(-60%);
	}

	.step.active p {
		background: white;
		color: black;
	}

	:global(.step .bold) {
		font-family: var(--sans);
	}

	@media (max-width: 1200px) {
		.chart-container-scrolly {
			position: sticky;
			top: calc(50vh - 275px);
			width: 100%;
			max-width: 600px;
			margin: 2rem auto;
		}

		.chart-container {
			display: flex;
			justify-content: center;
			width: 100%;
		}

		section,
		h2,
		h3,
		p {
			margin: 1rem;
		}

		section p {
			font-size: 18px;
		}

		.step {
			margin-left: 0;
			padding: 0 1rem;
			justify-content: center;
		}

		.step p {
			width: 100%;
			max-width: 600px;
			margin: 0 auto;
			text-align: center;
			transform: none;
		}
	}
</style>