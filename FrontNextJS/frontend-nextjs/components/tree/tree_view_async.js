'use client'

import React, { useState } from 'react';
import { Tree } from 'antd';
const { DirectoryTree } = Tree;
import BiIcon from '../util/bi_icon';
import TreeNode from './tree_node';
import { backend_root } from '@/app/config/global';

const TreeViewAsync = ({
  defaultExpandAll = false,
  rootUrl,
  nodeUrl,
  icon = <BiIcon bicode='node-plus' />
}) => {
  const [treeData, setTreeData] = useState([]);

  const updateTreeData = (list, key, children) =>
    list.map((node) => {
      if (node.key === key) {
        return {
          ...node,
          children,
        };
      }
      if (node.children) {
        return {
          ...node,
          children: updateTreeData(node.children, key, children),
        };
      }
      return node;
    });

  const onLoadData = ({ key, children }) =>
    new Promise((resolve) => {
      console.log('key: ', key);
      console.log('children: ', children);
      if (children) {
        resolve();
        return;
      }
      fetch(`${backend_root}/${nodeUrl}/${key}/children/`)
        .then((response) => response.json())
        .then((data) => {
          setTreeData((origin) =>
            updateTreeData(origin, key, data.map((node) => ({
              title: node.title,
              key: node.key.toString(),
              icon: icon,
              color: node.color,
              count: node.count,
              isLeaf: node.isLeaf,
            }))),
          );
          console.log('fetched node data: ', data)
          resolve();
        })
        .catch((error) => {
          console.error('Error loading tree node:', error);
          resolve();
        });
    });

  const renderTitle = ((nodeData) => {
    return <TreeNode
      title={nodeData.title}
      icon={icon}
      id={nodeData.key}
      color={nodeData.color}
      count={nodeData.count}
      href={`/tags/${nodeData.key}`}
    />
  })

  useState(() => {
    fetch(`${backend_root}/${rootUrl}`)
      .then((response) => response.json())
      .then((data) => {
        setTreeData(data.map((node) => ({
          title: node.title,
          key: node.key.toString(),
          icon: icon,
          color: node.color,
          count: node.count,
          isLeaf: node.isLeaf,
        })));
        console.log('fetched root data ', data)
      })
      .catch((error) => {
        console.error('Error loading tree root:', error);
      });
  }, []);

  return <Tree
    showLine
    titleRender={renderTitle}
    defaultExpandAll={defaultExpandAll}
    loadData={onLoadData}
    treeData={treeData}
  />;
};

export default TreeViewAsync;
