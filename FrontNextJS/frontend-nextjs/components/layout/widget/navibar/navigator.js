'use client'
import { site_title } from "@/app/config/global"
import Navibar from "./navibar"
import Link from "next/link"

export default function Navigator({ title='iMageLore', items={} }) {
  const navi_item = [
    {
      href: "/",
      text: '上传文件'
    },
    {
      href: "/posts/",
      text: '图片库'
    },
    {
      href: "/tags/",
      text: '标签'
    },
    {
      href: "/folders/",
      text: '文件夹'
    },
    {
      href: "/search/",
      text: '搜索'
    },
    {
      href: "/admin/",
      text: '站点管理'
    },
    {
      href: "/",
      text: '账户'
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