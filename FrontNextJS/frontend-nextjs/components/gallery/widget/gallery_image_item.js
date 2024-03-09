'use client'
import { site_title, backend_root } from "@/app/config/global"
import Image from "next/image";
import Link from "next/link"

export default function GalleryImageItem({ id = 1, alt = '图片加载中', href, src, borderColor = '#8877dd' }) {
  const getRandomInt = (max) => {
    return Math.floor(Math.random() * max);
}
  return (
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
  )
}