'use client'
import NavibarItem from "./navibar_item"

export default function Navibar({ items = [] }) {
  let i = 1;
  for(const item of items) {
    item.id=i;
    i += 1;
  }
  console.log(items)
  return (
    <ul className="navbar-nav me-auto">
      {items.map((item) => (
        <NavibarItem key={item.id} id={item.id} href={item.href} text={item.text} icon={item.icon}/>
      ))}
    </ul>
  )
}