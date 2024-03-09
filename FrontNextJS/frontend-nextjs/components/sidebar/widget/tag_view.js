import React from 'react';
import { Flex, Tag } from 'antd';
import Link from 'next/link';
import BiIcon from '@/components/util/bi_icon';

export default function TagView({
    tags = [{ id: 1, name: '这是标签', color: '#fe78ad', count: 114 }]
}) {
    console.log('TagView.tags: ', tags)
    tags.map((tag) => {
        console.log('TagView.tags.tag: ', tag)
    })
    console.log('TagView.tags-after: ', tags)

    return (
        <>
            <Flex gap="small" wrap="wrap">
                {tags.map((tag) => (
                    <Link
                        href={`/tags/${tag.id}`}
                        key={tag.id}
                    >
                        <Tag color={tag.color}>
                            <div classname='p-3'>
                                <span>
                                    <BiIcon bicode="tag-fill" />
                                    {tag.name}
                                </span>
                                <span id='tree_CountMarker' className=''>
                                    {tag.count}
                                </span>
                            </div>
                        </Tag>
                    </Link>
                ))}
            </Flex>
        </>
    )

}