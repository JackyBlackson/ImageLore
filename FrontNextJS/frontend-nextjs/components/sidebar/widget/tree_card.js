'use client'

import TreeViewAsync from "../../tree/tree_view_async";
import Card from "./card";
import BiIcon from "@/components/util/bi_icon";
import React, { useState } from 'react';

export default function TreeCard(
    title = '树形内容卡片',
    icon = <BiIcon bicode="tree" />,
    rootUrl = '/tags/roots',
    nodeUrl = "/tags"
) {

    return (
        <Card
            title={title}
            icon={icon}
            content={
                <div>
                    <TreeViewAsync
                        rootUrl={rootUrl}
                        nodeUrl={nodeUrl}
                    />
                </div>
            }
        />
    )
}