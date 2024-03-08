'use client'
import { useState, useEffect } from 'react';
import { Pagination } from 'antd';
import AlertStatic from '../util/alert_static';
import GalleryImageItem from './widget/gallery_image_item';
import { backend_root } from '@/app/config/global';

const ImageGallery = ( {apiUrl='api/posts/images', searchParam=''} ) => {
  const [images, setImages] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    const fetchImages = async () => {
      try {
        console.log('request at: ', `${backend_root}/${apiUrl}?${searchParam}&page=${currentPage}`)
        const response = await fetch(`${backend_root}/${apiUrl}?${searchParam}&page=${currentPage}`);
        const data = await response.json();
        setImages(data.results);
        setTotalPages(data.count);
        console.log('返回数据：', data)
        console.log('图片数量', data.count / data.results.length)
        console.log('分页数量：', Math.ceil(data.count / data.results.length))
      } catch (error) {
        console.error('Error fetching images:', error);
      }
    };

    fetchImages();
  }, [currentPage]);

  const handlePageChange = (page) => {
    setCurrentPage(page);
  };

  return (
    <>
      <div className="d-flex justify-content-around flex-wrap align-self-center">
        {images.map((image) => (
          <GalleryImageItem
            id={image.id}
            alt={image.name}
            href={`/posts/${image.id}`}
            src={backend_root + image.thumbnail_medium}
            borderColor={image.color}
          />
        ))}
        {images.length === 0 && (
          <AlertStatic type={'info'} text={
            <div className="alert alert-warning">
              <strong>{'目前网站上没有图片哦 >_>'}</strong>{' 快点击上方导航栏上传第一张图片吧！'}
            </div>
          } />
        )}
      </div>
      <div className="d-flex justify-content-center p-3">
          <Pagination current={currentPage} total={totalPages} onChange={handlePageChange} style={{ textAlign: 'center' }}  />
      </div>
    </>
  );
};

export default ImageGallery;