import Image from "next/image";
import "bootstrap/dist/css/bootstrap.min.css";
import ImageGallery from "@/components/gallery/image_gallery";
import BodySidebarLayout from "@/components/layout/body_sidebar_layout";
import Sidebar from "@/components/sidebar/siddebar";
import TagTreeCard from "@/components/sidebar/widget/tree_card";
import DefaultSidebar from "@/components/sidebar/default_sidebar";
import Home from "../page";
import RootLayout from "../layout";
import { site_title } from "../config/global";

export const metadata = {
  title: `图片库 - ${site_title}`,
  description: '使用文件夹与标签的图片库网站',
}

export default function PostPage() {
  return (

    <ImageGallery />

    )
}