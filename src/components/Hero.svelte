<script>
    import BouncingBalls from "./Bouncing.svelte";
  </script>
  
  <div class="hero-banner">
    <!-- GitHub link with logo -->
    <a
      class="github-link"
      href="https://github.com/jstonge/master-equations/"
      target="_blank"
      rel="noopener noreferrer"
    >
      <img
        src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
        alt="GitHub Logo"
      />
    </a>
  
    <div class="hero-content">
      <h1>Networks, Fast and Slow</h1>
      
      <div class="centered-layout">
        <div class="text-block">
          <p>Networks are powerful because they let us study both the structure and dynamics of social systems. How far your gossip travels, how quickly a disease spreads, or whether an idea catches on all depend not just on who is involved — but how they are connected. Yet, modelers often simplify these systems by focusing on the average behavior of a process, as if interactions happen at random.</p>
          <p>Social contact patterns are far from random. Some interactions are fleeting, like a conversation with a stranger on a train. Others are deeply persistent, like sharing a household or workplace. These differences matter — and they define two fundamentally different modeling regimes; <strong><u>annealed</u></strong> and <strong><u>quenched</u></strong> networks</p>
        </div>
        <div>
          <BouncingBalls width={600} height={350} />
        </div>
      </div>
    </div>
  </div>
  
  <style>


    /* Full-height hero with background gradient */
    .hero-banner {
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 1rem;
    }

      
    /* GitHub link positioning */
    .github-link {
      position: absolute;
      top: 1rem;
      right: 1rem;
      z-index: 3;
    }
  
    .github-link img {
      width: 40px;
      height: 40px;
      transition: transform 0.2s ease;
    }
  
    .github-link img:hover {
      transform: scale(1.1);
    }
  
    /* The semi-transparent content wrapper */
    .hero-content {
      border-radius: 10px;
      max-width: 1200px; /* control the width if desired */
      width: 80%;        /* responsive for wide screens */
      text-align: center;
    }
  
    .hero-content h1 {
        margin: 0 0 rem;
        font-size: 2.5rem;
        margin-top: 1rem;
        font-weight: bold;
    }
    

    .hero-content p {
        color: #5e5a5a;
        font-size: 1.2rem;
        font-style: italic;
    }
    
    /* Your row layout: text on the left, chart on the right */
    .centered-layout {
      display: flex;
      justify-content: center;
      gap: 2rem;
      margin: 5rem auto;
    }
  
    .text-block {
            max-width: 400px;
            margin: 0 auto; /* center the text block in its column */
            text-align: center; /* a bit more readable vs. center alignment */
        }
        
    /* Stack vertically on smaller screens */
    @media (max-width: 1200px) {

      .centered-layout {
        flex-direction: column;
        align-items: center;
        margin: 2rem auto;
      }
    
    .text-block {
        max-width: 600px; /* widen if you prefer on mobile */
        }
    }
  </style>
  