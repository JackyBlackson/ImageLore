'use client'

import { useState, useEffect } from 'react';
import { backend_root } from '@/app/config/global';
import Card from './widget/card';
import BiIcon from '../util/bi_icon';
import TagView from './widget/tag_view';
import AlertStatic from '../util/alert_static';

export default function CardImageDetail({ imageId = 12 }) {
    const [ready, setReady] = useState(false)
    const [image, setImage] = useState({})
    const [uploader, setUploader] = useState({})
    const [folder, setFolder] = useState({})
    const [tagList, setTagList] = useState([])

    useEffect(() => {
        if (!ready) {
            /*
                [
                    {
                        "id": 4,
                        "name": "小式建筑",
                        "color": "#0035AF"
                    },
                    {
                        "id": 3,
                        "name": "大式建筑",
                        "color": "#0035AF"
                    }
                ]
            */
            const fetchTags = async () => {
                try {
                    const response = await fetch(`${backend_root}/api/posts/images/${imageId}/tags`);
                    const data = await response.json();
                    setTagList(data)
                    console.log('tagList: ', data)
                } catch (error) {
                    console.error('Error fetching images:', error);
                }
            }


            /*
            {
                "id": 1,
                "username": "21301052",
                "email": "Jacky_Blackson@outlook.com"
            }
            */
            const fetchUploader = async (img_data) => {
                try {
                    const response = await fetch(`${backend_root}/api/users/${img_data.uploader}`);
                    const data = await response.json();
                    setUploader(data)
                    console.log('data: ', img_data)
                } catch (error) {
                    console.error('Error fetching images:', error);
                }
            };

            /*
            {
                "id": 1,
                "name": "test_base",
                "description": "这是测试的根目录",
                "date_created": "2024-02-29T15:23:35.439588Z",
                "last_modified": "2024-02-29T15:23:35.439588Z",
                "color": "#0035AF",
                "count": 0,
                "creator": 1,
                "father": null
            }
            */
            const fetchFolder = async (img_data) => {
                try {
                    const response = await fetch(`${backend_root}/api/folders/${img_data.folder}`);
                    const data = await response.json();
                    setFolder(data)
                } catch (error) {
                    console.error('Error fetching images:', error);
                }
            };

            /*
            {
                "uploader": 3,
                "name": "斗拱",
                "description": "这是测试的根目录",
                "folder": 1,
                "color": "#114514",
                "image": "http://localhost:8000/media/images/2023-12-20_21.06.45.png",
                "thumbnail_small": "/media/thumbnails/small/%E6%96%97%E6%8B%B1_small.jpg",
                "thumbnail_medium": "/media/thumbnails/medium/%E6%96%97%E6%8B%B1_medium.jpg"
            }
            */
            const fetchImages = async () => {
                try {
                    const response = await fetch(`${backend_root}/api/posts/images/${imageId}`);
                    const data = await response.json();
                    setImage(data)
                    await fetchUploader(data)
                    await fetchFolder(data)
                    //await fetchTags()
                } catch (error) {
                    console.error('Error fetching images:', error);
                }
            };






            fetchImages();
            setReady(true);
            fetchTags()
        }
    }, [ready, imageId]);

    const content = <table className="table table-hover text-center">
        <tbody>
            <tr>
                <td className="text-nowrap font-weight-bold">图片序号</td>
                <td className='text-break'>
                    <div>
                        <code>post.id = </code>
                        <kbd>{image.id}</kbd>
                    </div>
                </td>
            </tr>
            <tr>
                <td className="text-nowrap font-weight-bold">上传用户</td>
                <td className='text-break'>
                    <div>{uploader.username}</div>
                </td>
            </tr>
            <tr>
                <td className="text-nowrap font-weight-bold">图片名称</td>
                <td className='text-break'>
                    <div>{image.name}</div>
                </td>
            </tr>

            <tr>
                <td className="text-nowrap font-weight-bold">图片描述</td>
                <td className='text-break'>
                    <div>{image.description}</div>
                </td>
            </tr>
            <tr>
                <td className="text-nowrap font-weight-bold">所属文件夹</td>
                <td className='text-break'>
                    <div className="color_area" style={{ backgroundColor: folder.color }}>{folder.name}</div>
                </td>
            </tr>
            <tr>
                <td className="text-nowrap font-weight-bold">颜色标记</td>
                <td className='text-break'>
                    <div className="color_area" style={{ backgroundColor: image.color }}>{image.color}</div>
                </td>
            </tr>
            <tr>
                <td className="text-nowrap font-weight-bold">相关标签</td>
                <td className='text-break'>
                    {tagList.length > 0
                        ?
                        <TagView tags={tagList} />
                        :
                        <AlertStatic
                            type='info'
                            strong='没有相关标签。'
                            text='你需要为这张图片添加相关的标签，这里才会显示标签信息。'
                        />
                    }
                </td>
            </tr>
        </tbody>
    </table>
    const title = '图片详细信息'
    const icon = <BiIcon bicode="info-circle" />

    return (
        <Card
            title={title}
            icon={icon}
            content={content}
        />
    )

}