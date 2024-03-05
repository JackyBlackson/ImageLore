import Link from "next/link";
import BiIcon from "../util/bi_icon";

export default function TreeNode({
    color = '#8877dd',
    icon = <BiIcon bicode="node-plus" />,
    href = '#',
    key = 0,
    title = 'This is a NODE!'
}) {
    return (

        <Link href={href} style={{textDecoration: 'none'}}>
            <div className='color_area' style={{ 'background-color': color}}>
                {icon}
                {title}
            </div>
        </Link >

    )
}