// layouts/forceDirected.js
import { forceSimulation, forceManyBody, forceCenter, forceLink, forceCollide } from "d3-force";

export function forceDirectedLayout({ nodes, links, width, height, iterations = 1000 }) {
  const simulation = forceSimulation(nodes)
    .force("link", forceLink(links).id(d => d.id).distance(80).strength(0.1))
    .force("charge", forceManyBody().strength(-100))
    .force("center", forceCenter(width, height / 1.5))
    .force("collision", forceCollide(15))
    .stop();

  for (let i = 0; i < iterations; ++i) simulation.tick();
  return simulation.nodes(); // nodes now have updated x/y
}
