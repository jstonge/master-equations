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
      <h1>Hello master equations</h1>
  
      <div class="centered-layout">
        <div class="text-block">
          <h3>We investigate annealed networks and their relationship to so-called quenched.</h3>
          <h3>On the right, we have the most quintessential example of a contagion: the billiard ball world.</h3>
          <h3>We argue this is all wrong, but not for the same reason as usual.</h3>
        </div>
        <div>
          <BouncingBalls width={600} height={300} />
        </div>
      </div>
    </div>
  </div>
  
  <style>

     h1 {
        font-size: 2.5rem;
        font-weight: bold;
        text-transform: uppercase;

    }       

    h3 {
        color: #aaa8a8;
        font-size: 1.5rem;
        font-style: italic;
    }


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
         margin-top: 0;
        font-weight: bold;
        text-transform: uppercase;
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
  