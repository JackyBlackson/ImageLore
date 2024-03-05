'use client'
import Link from "next/link"

export default function NavibarItem({ href='/', text='导航项' }) {
  return (
    <li className="nav-item">
      <Link className="nav-link" href={href}>
        <i className="bi bi-cloud-upload"></i>
        {text}
      </Link>
    </li>
  )
}