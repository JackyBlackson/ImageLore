import Link from "next/link";
import BiIcon from "../util/bi_icon";
import { Button, Popover, ConfigProvider, Flex } from 'antd';

export default function TreeNode({
    color = '#8877dd',
    icon = <BiIcon bicode="node-plus" />,
    href = '#',
    id = 0,
    title = 'This is a NODE!',
    count = 0,
    targetType = 'tags',
}) {

    const deleteContent = <div>
        <div className='m-1'>
            <Button type="default" danger>
                <div><BiIcon bicode="trash3" />{icon}删除并将子项目上移</div>
            </Button>
        </div>
        <div className='m-1'>
            <Button type="dashed" danger>
                <div><BiIcon bicode="trash3" />{icon}级联删除（危险！）</div>
            </Button>
        </div>
    </div>

    const content = <div>
        <div className='m-1'>
            <Button type="primary">
                <div><BiIcon bicode="arrow-bar-down" />{icon}新建并列项</div>
            </Button>
        </div>
        <div className='m-1'>
            <Button type="primary">
                <div><BiIcon bicode="arrow-return-right" />{icon}新建子项</div>
            </Button>
        </div>
        <Popover title={`删除选项`} content={deleteContent} trigger="click">
            <div className='m-1'>
                <Button type="dashed" danger>
                    <div><BiIcon bicode="trash3" />{icon}删除</div>
                </Button>
            </div>
        </Popover>
    </div>

    return (

        <Popover title={`${title} 操作`} content={content}>
            <Link href={href} style={{ textDecoration: 'none' }} >
                <div className='color_area' style={{ textDecoration: 'none', backgroundColor: color }}>
                    <span>
                        {icon}
                        {title}
                    </span>
                    <span id='tree_CountMarker' style={{ marginLeft: '5px' }}>
                        {/* <BiIcon bicode="bookmark-fill" /> */}
                        ({count})
                    </span>
                </div>
            </Link >
        </Popover>

    )
}