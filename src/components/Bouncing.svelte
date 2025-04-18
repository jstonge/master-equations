<script>
  import P5 from '$lib/P5.svelte';
  
  // let numBalls = $state(50);
  const RED_DURATION = 6000;

  let {width, height, numBalls} = $props()
  
  const sketch = (p5) => {
    let balls = [];

    class Ball {
      constructor(x, y, vx, vy, r = 10, red = false) {
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
        this.r = r;
        this.redTime = red ? p5.millis() : null;
        this.becameRedThisFrame = false;
      }

      isRed() {
        if (this.redTime === null) return false;
        return p5.millis() - this.redTime < RED_DURATION;
      }

      move() {
    this.x += this.vx;
    this.y += this.vy;

    if (this.x < this.r) {
      this.vx *= -1;
      this.x = this.r;
    } else if (this.x > p5.width - this.r) {
      this.vx *= -1;
      this.x = p5.width - this.r;
    }

    if (this.y < this.r) {
      this.vy *= -1;
      this.y = this.r;
    } else if (this.y > p5.height - this.r) {
      this.vy *= -1;
      this.y = p5.height - this.r;
    }
  }


      display() {
        p5.fill(this.isRed() ? '#ff4d4d' : 'black');
        p5.strokeWeight(1.2);
        p5.ellipse(this.x, this.y, this.r * 2);
      }

      checkCollision(other) {
        const dx = other.x - this.x;
        const dy = other.y - this.y;
        const dist = Math.hypot(dx, dy);
        const minDist = this.r + other.r;

        if (dist < minDist) {
          // Infection logic — allow either to infect the other
          if ((this.isRed() || this.becameRedThisFrame) && !other.isRed()) {
            other.redTime = p5.millis();
            other.becameRedThisFrame = true;
          }
          if ((other.isRed() || other.becameRedThisFrame) && !this.isRed()) {
            this.redTime = p5.millis();
            this.becameRedThisFrame = true;
          }

          // Handle bounce
          const angle = Math.atan2(dy, dx);
          const sin = Math.sin(angle);
          const cos = Math.cos(angle);

          const v1 = rotate(this.vx, this.vy, sin, cos, true);
          const v2 = rotate(other.vx, other.vy, sin, cos, true);

          const temp = v1.x;
          v1.x = v2.x;
          v2.x = temp;

          const final1 = rotate(v1.x, v1.y, sin, cos, false);
          const final2 = rotate(v2.x, v2.y, sin, cos, false);

          this.vx = final1.x;
          this.vy = final1.y;
          other.vx = final2.x;
          other.vy = final2.y;

          // Prevent overlap
          const overlap = 0.5 * (minDist - dist + 0.1);
          this.x -= overlap * (dx / dist);
          this.y -= overlap * (dy / dist);
          other.x += overlap * (dx / dist);
          other.y += overlap * (dy / dist);
        }
      }
    }

    function rotate(vx, vy, sin, cos, reverse) {
      return reverse
        ? { x: vx * cos + vy * sin, y: vy * cos - vx * sin }
        : { x: vx * cos - vy * sin, y: vy * cos + vx * sin };
    }

    let prevNumBalls = null;

    p5.setup = () => {
      p5.createCanvas(width, height);
      initBalls();
    };

    function initBalls() {
      balls = [];
      for (let i = 0; i < numBalls; i++) {
        const isInitialRed = i === 0;
        balls.push(
          new Ball(
            p5.random(50, p5.width - 50),
            p5.random(50, p5.height - 50),
            p5.random(-2, 2),
            p5.random(-2, 2),
            7,
            isInitialRed
          )
        );
      }
      prevNumBalls = numBalls;
    }

    p5.draw = () => {
      p5.background('#f9f9f9');

      if (numBalls !== prevNumBalls) {
        initBalls();
      }

      for (let i = 0; i < balls.length; i++) {
        const b = balls[i];
        b.move();
        b.display();

        for (let j = i + 1; j < balls.length; j++) {
          b.checkCollision(balls[j]);
        }
      }

      // Reset infection flag after all checks
      for (let b of balls) {
        b.becameRedThisFrame = false;
      }
    };
  };
</script>


<P5 {sketch} />


<style>
  :global(canvas) {
    display: block;
    width: 100% !important;   /* override pixel size */
    height: auto !important;  /* maintain aspect ratio */
  }
</style>