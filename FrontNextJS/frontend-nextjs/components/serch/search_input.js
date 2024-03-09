'use client'

import React, { useState, useEffect } from 'react';
import { Mentions } from 'antd';
import { backend_root } from '@/app/config/global';
import Link from 'next/link';
import { usePathname, useSearchParams } from 'next/navigation'

const MOCK_DATA = {
  '@': ['afc163', 'zombiej', 'yesmeck'],
  '#': ['1.0', '2.0', '3.0'],
};
const SearchInput = () => {
  const [prefix, setPrefix] = useState('@');
  const [completionData, setCompletionData] = useState({});
  const [ready, setReady] = useState(false);
  const [content, setContent] = useState('*')
  const [tagList, setTagList] = useState([])
  const [userList, setUserList] = useState([])
  const [folderList, setFolderList] = useState([])


  useEffect(() => {
    if (!ready) {
      const fetchTags = async () => {
        try {
          const response = await fetch(`${backend_root}/api/tags/simple`);
          const data = await response.json();
          completionData['#'] = data
          console.log(completionData)
          setCompletionData(completionData)
          setTagList(data)
        } catch (error) {
          console.error('Error fetching tags:', error);
        }
      };

      const fetchUsers = async () => {
        try {
          const response = await fetch(`${backend_root}/api/users/simple`);
          const data = await response.json();
          completionData['@'] = data
          setCompletionData(completionData)
          setUserList(data)
        } catch (error) {
          console.error('Error fetching tags:', error);
        }
      };

      const fetchFolders = async () => {
        try {
          const response = await fetch(`${backend_root}/api/folders/simple`);
          const data = await response.json();
          completionData['/'] = data
          setCompletionData(completionData)
          setFolderList(data)
        } catch (error) {
          console.error('Error fetching tags:', error);
        }
      };


      fetchTags();
      fetchUsers();
      fetchFolders();
      setReady(true)
    }
  }, [completionData, ready]);

  

  const onSearch = (_, newPrefix) => {
    setPrefix(newPrefix);
  };

  const onChange = (value) => {
    value = value.replace(/\s/g, "");
    setContent(value)
    console.log('Change:', value);
  };

  let defaultText = ''
  const pathname = usePathname()
  if (pathname.indexOf("search") !== -1) {
    let split = pathname.split('/')
    
    defaultText = decodeURIComponent(split[split.length - 1])
  } else if (pathname.indexOf("tags") !== -1) {
    let split = pathname.split('/')
    let id = Number(split[split.length - 1])
    for (const tag in tagList) {
      if (tag.id === id) {
        defaultText = `#${tag.name}`
        break
      }
    }
  } else if (pathname.indexOf("folders") !== -1) {
    let split = pathname.split('/')
    let id = Number(split[split.length - 1])
    for (const folder in folderList) {
      if (folder.id === id) {
        defaultText = `/${folder.name}`
        break
      }
    }
  }
  defaultText = defaultText.replace('+', ' + ')
  defaultText = defaultText.replace('-', ' - ')
  defaultText = defaultText.replace('&', ' & ')
  defaultText = defaultText.replace('|', ' | ')


  return (
    <div className="d-flex mb-3">
      <Mentions
        autoSize
        allowClear
        style={{
          width: '100%',
        }}
        placeholder="输入@来选择用户，输入#来选择标签，输入/来选择文件夹"
        defaultValue={defaultText}
        prefix={['@', '#', '/']}
        onSearch={onSearch}
        onChange={onChange}
        options={(completionData[prefix] || []).map((item) => ({
          value: item.name,
          key: item.name,
          label: `${item.name} ${item.count!==undefined? `(${item.count})` : ''}`,
          style: {color: item.color!==undefined?item.color:'black'}
        }))}
      />
      <Link href={`/search/${encodeURIComponent(content)}`} key={content}>
        <div
          className="btn btn-primary ml-3"
        >
          <i className="bi bi-search"></i>
        </div>
      </Link>
    </div>

  );
};
export default SearchInput;