'use client'
import NavibarItem from "./navibar_item"

export default function Navibar({ items = [] }) {
  return (
    <ul className="navbar-nav me-auto">
      {items.map((item) => (
        <NavibarItem href={item.href} text={item.text} icon={item.icon}/>
      ))}
    </ul>
  )
}