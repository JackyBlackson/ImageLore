import "bootstrap/dist/css/bootstrap.min.css";
import { site_title } from "@/app/config/global";
import ImageGallery from "@/components/gallery/image_gallery";

export const metadata = {
  title: `文件夹详情 - ${site_title}`,
  description: '使用文件夹与标签的图片库网站',
}

export default function TagDetailPage({ params }) {
  const id = params.id;
  return (
    <ImageGallery apiUrl={`folders/${id}/images`} />
  )
}