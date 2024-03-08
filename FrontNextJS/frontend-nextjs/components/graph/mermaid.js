"use client"

import React, { useEffect } from 'react';
import mermaid from 'mermaid';
import {flowchartClickCallback} from './tag_flow_chart_callback'

mermaid.initialize({
  startOnLoad: true,
  theme: 'default',
  securityLevel: 'loose',
});

const MermaidGraph = ({
  chart = `
  graph TD;
  A --> B;
  A --> C;
  B --> D;
  C --> D;
  `
}) => {
  useEffect(() => {
    console.log('USE EFFECT ON MERMAIDGRAPG: chart=', chart)
    mermaid.contentLoaded();
  }, []);
  mermaid.contentLoaded();
  mermaid.flowchartConfig = {
    width: '100%'
}
  return <div className="mermaid mermaid_div d-flex justify-content-center">{chart}</div>;
};

export default MermaidGraph;