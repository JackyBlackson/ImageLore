'use client'
import Link from "next/link"
import BiIcon from "@/components/util/bi_icon"

export default function NavibarItem({ id=1, href='/', text='导航项', icon='cloud-upload'}) {
  return (
    <li key={id} className="nav-item">
      <Link className="nav-link" href={href}>
        <BiIcon bicode={icon} />
        {text}
      </Link>
    </li>
  )
}