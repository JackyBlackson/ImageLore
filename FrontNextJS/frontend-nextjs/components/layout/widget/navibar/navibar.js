'use client'
import NavibarItem from "./navibar_item"

export default function Navibar({ items = [] }) {
  return (
    <ul className="navbar-nav me-auto">
      {items.map((item) => {
        <NavibarItem href={item.href} text={item.text} />
      })}
      <li className="nav-item">
        <a className="nav-link" href="/">
          <i className="bi bi-cloud-upload"></i>
          上传文件
        </a>
      </li>
      <li className="nav-item">
        <a className="nav-link" href="/posts/">
          <i className="bi bi-card-image"></i>
          图片库
        </a>
      </li>
      <li className="nav-item">
        <a className="nav-link" href="/tags/">
          <i className="bi bi-tags"></i>
          标签
        </a>
      </li>
      <li className="nav-item">
        <a className="nav-link" href="/folders/">
          <i className="bi bi-folder-symlink"></i>
          文件夹
        </a>
      </li>
      <li className="nav-item">
        <a className="nav-link" href="/search/">
          <i className="bi bi-search"></i>
          搜索
        </a>
      </li>
      <li className="nav-item">
        <a className="nav-link" href="/admin/">
          <i className="bi bi-magic"></i>
          站点管理
        </a>
      </li>
      <li className="nav-item">
        <a className="nav-link" href="/">
          <i className="bi bi-house"></i>
          账户
        </a>
      </li>
    </ul>
  )
}