'use client'

import { useState, useEffect } from 'react';
import { Divider, Form, Radio, Skeleton, Space, Switch } from 'antd';
import { Slider } from 'antd';
import Link from 'next/link';

export default function DetailBigImage({ itemUrl }) {
    const [image, setImage] = useState('')
    const [color, setColor] = useState('')
    const [ready, setReady] = useState(false)
    const [maxHeight, setMaxHeight] = useState(100)
    const [resizable, setResizable] = useState(true)

    const getRandomInt = (max) => {
        return Math.floor(Math.random() * max);
    }

    const onResize = ((size) => {
        setMaxHeight(size)
    })

    const onChange = (checked) => {
        setMaxHeight(100);
        setResizable(checked);
    };

    useEffect(() => {
        if (!ready) {
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
        }
    });
    return (
        <div className='container-fluid text-center'>
            <div className="container">
                <span>
                    <Slider
                        defaultValue={100}
                        disabled={!resizable}
                        onChange={onResize}
                        max={100}
                        min={5}
                    /></span>
            </div>
            <div className="align-self-center">
                <div className="d-flex justify-content-around flex-wrap align-self-center image-container">


                    <div>
                        {
                            ready ?
                                <Link href={image}>
                                    <img id="image"
                                        className="post_list"
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