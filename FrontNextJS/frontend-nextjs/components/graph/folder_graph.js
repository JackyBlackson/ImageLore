"use client"

import { useState, useEffect } from 'react';
import { api_root } from '@/app/config/global';
import GraphView from './graph_view';
import AlertStatic from '../util/alert_static';
import {flowchartClickCallback} from './tag_flow_chart_callback'

export default function FolderGraph({ apiUrl = 'folders/relations' }) {
  const [ready, setReady] = useState(false)
  const [relations, setRelations] = useState({})
  const [graphContent, setGraphContent] = useState(null)

  useEffect(() => {
    /*
      [
          {
              "title": "test_base",
              "value": 1,
              "key": 1,
              "children": [
                  {
                      "title": "一级文件夹",
                      "value": 2,
                      "key": 2,
                      "children": [
                          {
                              "title": "二级文件夹",
                              "value": 3,
                              "key": 3
                          }
                      ]
                  }
              ]
          }
      ]
    */
    const convertGraphContent = (data) => {
      let content = 'graph LR;'

      const folder_list = data.folder_list
      console.log('tag_list: ', folder_list)

      const primary = data.primary
      console.log('primary: ', primary)

      const secondary = data.secondary
      console.log('secondary: ', secondary)

      const strong = data.strong

      for (const item of folder_list) {
        content += `    id${item.id}([\"${item.name} (${item.count})\"]);`
      }

      for (const item of primary) {
        content += `    id${item.father.id} --> id${item.child.id};`
      }
      for (const item of secondary) {
        content += `    id${item.father.id} -.\"${item.description}\".- id${item.child.id};`
      }
      for (const item of folder_list) {
        content += `    style id${item.id} stroke:${item.color},stroke-width:2px;`
        content += `    click id${item.id} href \"/folders/${item.id}\" \"点击查看“${item.name}”标签的详情\";`
        //content += `    click id${item.id} call callback(${item.id});`;
      }

      setGraphContent(content)
    }
    if (!ready) {
      const fetchRelations = async () => {
        try {
          const response = await fetch(`${api_root}/${apiUrl}`);
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
  }, [ready, apiUrl]);

  if (graphContent) {
    console.log(graphContent)
    return (<GraphView
      chart={graphContent}
    />)
  } else {
    return (
      <AlertStatic
        type='info'
        strong='正在加载标签图谱'
        text='请稍后，待数据加载完毕，图谱将会正常显示。'
      />
    )
  }
}