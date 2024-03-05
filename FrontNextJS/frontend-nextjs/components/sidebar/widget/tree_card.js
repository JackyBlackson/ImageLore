'use client'

import TreeViewAsync from "../../tree/tree_view_async";
import Card from "./card";
import BiIcon from "@/components/util/bi_icon";
import { backend_root } from "@/app/config/global";
import React, { useState } from 'react';
import { Switch } from "antd";

export default function TreeCard(
    title = '树形内容卡片',
    icon = <BiIcon bicode="tree" />,
    rootUrl = '/api/tags/roots',
    nodeUrl = "/api/tags"
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