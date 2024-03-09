'use client'
import Image from "next/image";
import Link from "next/link"
import { Badge, Card, Space } from 'antd';
import BiIcon from "@/components/util/bi_icon";

export default function GalleryImageItem({ 
  id = 1, 
  alt = '图片加载中', 
  href, 
  src, 
  borderColor = '#8877dd' ,
  folder = '无文件夹',
  tagCount = 0
}) {
  const ribbonText = <div>
    <span className='m-1'>
      <BiIcon bicode='folder' />
      {folder}
    </span>
    <span className='m-1'>
      <BiIcon bicode='tags' />
      {tagCount}
    </span>
  </div>
  return (
    <Badge.Ribbon text={ribbonText} color={borderColor} >
      <div key={id} className="pt-2 align-self-center">
        <Link href={href}>
          <img
            className="post_list"
            src={src}
            alt={alt}
            style={{ borderColor: borderColor }}
          />
        </Link>
      </div>
    </Badge.Ribbon>
  )
}