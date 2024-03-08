import Link from "next/link";
import BiIcon from "../util/bi_icon";

export default function TreeNode({
    color = '#8877dd',
    icon = <BiIcon bicode="node-plus" />,
    href = '#',
    id = 0,
    title = 'This is a NODE!',
    count = 0,
    targetType='tags',
}) {
    return (

        <Link href={href} style={{textDecoration: 'none'}} >
            <div className='color_area' style={{ textDecoration: 'none',  backgroundColor: color  }}>
                <span>
                    {icon}
                    {title}
                </span>
                <span id='tree_CountMarker' style={{marginLeft: '5px'}}>
                    {/* <BiIcon bicode="bookmark-fill" /> */}
                    ({count})
                </span>
            </div>
        </Link >

    )
}