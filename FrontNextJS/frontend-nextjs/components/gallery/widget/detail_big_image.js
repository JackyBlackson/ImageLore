'use client'

import { useState, useEffect } from 'react';
import { backend_root } from '@/app/config/global';
import { Divider, Form, Radio, Skeleton, Space, Switch } from 'antd';
import DisabledContext from 'antd/es/config-provider/DisabledContext';
import { Slider } from 'antd';
import Link from 'next/link';

export default function DetailBigImage({ itemUrl }) {
    const [image, setImage] = useState('')
    const [color, setColor] = useState('')
    const [ready, setReady] = useState(false)
    const [maxHeight, setMaxHeight] = useState(100)
    const [resizable, setResizable] = useState(true)

    const onResize = ((size) => {
        setMaxHeight(size)
    })

    const onChange = (checked) => {
        setMaxHeight(100);
        setResizable(checked);
    };

    useEffect(() => {
        const fetchImages = async () => {
            try {
                const response = await fetch(itemUrl);
                const data = await response.json();
                setImage(data.image)
                setColor(data.color)
                setReady(true)
            } catch (error) {
                console.error('Error fetching images:', error);
            }
        };



        fetchImages();
    });
    return (
        <div class='container-fluid text-center'>
            <div class="container">
                <span>
                    <Slider
                        defaultValue={100}
                        disabled={!resizable}
                        onChange={onResize}
                        max={100}
                        min={5}
                    /></span>
            </div>
            <div class="align-self-center">
                <div class="d-flex justify-content-around flex-wrap align-self-center image-container">


                    <div>
                        {
                            ready ?
                                <Link href={image}>
                                    <img id="image"
                                        class="post_list"
                                        src={image}
                                        alt="正在加载图片。。。"
                                        style={{ "border-color": color, width: `${maxHeight}%` }} />
                                </Link>
                                :
                                <div style={{ 'width': '100%' }}>
                                    <Skeleton.Image active={ready} />
                                </div>
                        }
                    </div>
                </div>
            </div>
        </div>
    )
}