'use client'
import Link from "next/link"
import BiIcon from "@/components/util/bi_icon"

export default function NavibarItem({ href='/', text='导航项', icon='cloud-upload'}) {
  return (
    <li className="nav-item">
      <Link className="nav-link" href={href}>
        <BiIcon bicode={icon} />
        {text}
      </Link>
    </li>
  )
}