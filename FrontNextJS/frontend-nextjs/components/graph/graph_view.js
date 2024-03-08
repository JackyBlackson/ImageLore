import React from "react"
import MermaidGraph from "./mermaid"

export default function GraphView({ 
  chart = `
  graph TD;
  A-->B;
  A-->C;
  B-->D;
  C-->D;
  `
}) {
  return (
    < MermaidGraph
  chart = {chart} />
  )
}