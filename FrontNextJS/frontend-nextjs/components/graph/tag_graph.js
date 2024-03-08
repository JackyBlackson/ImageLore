"use client"

import { useState, useEffect } from 'react';
import { backend_root } from '@/app/config/global';
import GraphView from './graph_view';
import AlertStatic from '../util/alert_static';
import {flowchartClickCallback} from './tag_flow_chart_callback'

export default function TagGraph({ apiUrl = 'api/tags/relations' }) {
  const [ready, setReady] = useState(false)
  const [relations, setRelations] = useState({})
  const [graphContent, setGraphContent] = useState(null)

  useEffect(() => {
    /*
    {
      "tag_list": [
        {
            "id": 1,
            "name": "明清官式建筑",
            "color": "#000000",
            "count": 4
        },
    ],
      "primary": [
          {
              "father": {
                  "id": 1,
                  "name": "明清官式建筑",
                  "color": "#000000",
                  "count": 4
              },
              "child": {
                  "id": 3,
                  "name": "大式建筑",
                  "color": "#0035AF",
                  "count": 2
              }
          },
      ],
      "secondary": [
          {
              "description": "相同",
              "father": {
                  "id": 1,
                  "name": "明清官式建筑",
                  "color": "#000000",
                  "count": 4
              },
              "child": {
                  "id": 1,
                  "name": "明清官式建筑",
                  "color": "#000000",
                  "count": 4
              }
          },
      ]
  }
    */
    const convertGraphContent = (data) => {
      let content = 'graph TD;'

      const tag_list = data.tag_list
      console.log('tag_list: ', tag_list)

      const primary = data.primary
      console.log('primary: ', primary)

      const secondary = data.secondary
      console.log('secondary: ', secondary)

      const strong = data.strong

      for (const item of tag_list) {
        content += `    id${item.id}([\"${item.name} (${item.count})\"]);`
      }
    
      for (const item of primary) {
        content += `    id${item.father.id} --> id${item.child.id};`
      }
      for (const item of secondary) {
        content += `    id${item.father.id} -.\"${item.description}\".- id${item.child.id};`
      }
      for (const item of tag_list) {
        content += `    style id${item.id} stroke:${item.color},stroke-width:2px;`
        content += `    click id${item.id} href \"/tags/${item.id}\" \"点击查看“${item.name}”标签的详情\";`
        //content += `    click id${item.id} call callback(${item.id});`;
      }

      setGraphContent(content)
    }
    if (!ready) {
      const fetchRelations = async () => {
        try {
          const response = await fetch(`${backend_root}/${apiUrl}`);
          const data = await response.json();
          setRelations(data)
          console.log('relations: ', data)
          convertGraphContent(data)
          
        } catch (error) {
          console.error('Error fetching images:', error);
        }
      }
      fetchRelations();
      setReady(true);
    }
  });

  if(graphContent){
    console.log(graphContent)
    return (<GraphView
      chart={graphContent}
    />)
  } else {
    return(
      <AlertStatic
        type='info'
        strong='正在加载标签图谱'
        text='请稍后，待数据加载完毕，图谱将会正常显示。'
        />
    )
  }
}