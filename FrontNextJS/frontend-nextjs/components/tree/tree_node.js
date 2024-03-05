import Link from "next/link";
import BiIcon from "../util/bi_icon";

export default function TreeNode({
    color = '#8877dd',
    icon = <BiIcon bicode="node-plus" />,
    href = '#',
    key = 0,
    title = 'This is a NODE!',
    count = 0
}) {
    return (

        <Link href={href} style={{textDecoration: 'none'}} >
            <div className='color_area' style={{ textDecoration: 'none',  'background-color': color  }}>
                <span>
                    {icon}
                    {title}
                </span>
                <span id='tree_CountMarker' className=''>
                    {/* <BiIcon bicode="bookmark-fill" /> */}
                    {count}
                </span>
            </div>
        </Link >

    )
}