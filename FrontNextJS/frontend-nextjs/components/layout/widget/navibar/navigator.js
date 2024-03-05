'use client'
import { site_title } from "@/app/config/global"
import Navibar from "./navibar"
import Link from "next/link"

export default function Navigator({ title='iMageLore', items={} }) {
  const navi_item = [
    {
      href: "/",
      text: '上传文件',
      icon: 'cloud-upload',
    },
    {
      href: "/posts/",
      text: '图片库',
      icon: 'images',
    },
    {
      href: "/tags/",
      text: '标签',
      icon: 'tags',
    },
    {
      href: "/folders/",
      text: '文件夹',
      icon: 'folder2-open',
    },
    {
      href: "/search/",
      text: '搜索',
      icon: 'search',
    },
    {
      href: "/admin/",
      text: '站点管理',
      icon: 'toggles',
    },
    {
      href: "/",
      text: '账户',
      icon: 'person-lock',
    },
  ]
  return (
    <nav id="navigator" className="navbar navbar-expand-lg fixed-top bg-white box-shadow">
      <div className="container-fluid">
        <Link className="navbar-brand" href="/">
          <i className="bi bi-database"></i>
          {site_title}
        </Link>
        <button className="navbar-toggler bg-purple-700 rounded-3xl" type="button" data-bs-toggle="collapse" data-bs-target="#mynavbar">
          <i className="bi bi-list"></i>
        </button>
        <div className="collapse navbar-collapse" id="mynavbar">
          <Navibar items={navi_item} />
        </div>
      </div>
    </nav>
  )
}