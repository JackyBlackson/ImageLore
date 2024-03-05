'use client'

import Image from "next/image";
import "bootstrap/dist/css/bootstrap.min.css";
import ImageGallery from "@/components/gallery/image_gallery";
import BodySidebarLayout from "@/components/layout/body_sidebar_layout";
import Sidebar from "@/components/sidebar/siddebar";
import TagTreeCard from "@/components/sidebar/widget/tree_card";
import DetailBigImage from "@/components/gallery/widget/detail_big_image";
import { backend_root } from "@/app/config/global";
import DefaultSidebar from "@/components/sidebar/default_sidebar";


export default function Page({ params }) {
  const id = params.slug;
  return (
    

    <BodySidebarLayout
      body={<DetailBigImage itemUrl={`${backend_root}/api/posts/images/${id}`} />}
      sidebar={<DefaultSidebar />}
    />
  )
}