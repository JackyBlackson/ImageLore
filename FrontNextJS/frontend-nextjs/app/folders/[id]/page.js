import ImageGallery from "@/components/gallery/image_gallery"
import "bootstrap/dist/css/bootstrap.min.css";
import DetailBigImage from "@/components/gallery/widget/detail_big_image";
import { backend_root } from "@/app/config/global";
import { site_title } from "@/app/config/global";

export const metadata = {
  title: `文件夹详情 - ${site_title}`,
  description: '使用文件夹与标签的图片库网站',
}

export default function TagDetailPage({ params }) {
  const id = params.id;
  return (
    <ImageGallery apiUrl={`api/folders/${id}/images`} />
  )
}