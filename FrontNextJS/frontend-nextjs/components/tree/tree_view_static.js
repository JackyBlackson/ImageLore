import React, { useState, useEffect } from 'react';
import { Tree } from 'antd';
const { DirectoryTree } = Tree;

const TreeViewStatic = () => {
  const [treeData, setTreeData] = useState([])

  

  const onSelect = (keys, info) => {
    console.log('Trigger Select', keys, info);
  };
  const onExpand = (keys, info) => {
    console.log('Trigger Expand', keys, info);
  };

  return (
    <DirectoryTree
      multiple
      defaultExpandAll
      onSelect={onSelect}
      onExpand={onExpand}
      treeData={treeData}
    />
  );
};
export default App;