export function radialLayout({ nodes, links, width, height }) {
  const radius = Math.min(width / 2, height) / 1.5;

  // Position nodes in a circle
  nodes.forEach((node, i) => {
    const angle = (i / nodes.length) * 2 * Math.PI;
    node.x = width / 2 + radius * Math.cos(angle);
    node.y = height / 2 + radius * Math.sin(angle);
  });

  // Map for quick lookup
  const nodeMap = new Map(nodes.map(n => [n.id, n]));

  // Assign actual node references to link.source and link.target
  links.forEach(link => {
    link.source = nodeMap.get(link.source.id || link.source);
    link.target = nodeMap.get(link.target.id || link.target);
  });

  return nodes;
}
