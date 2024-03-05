import Image from "next/image";
import "bootstrap/dist/css/bootstrap.min.css";
import ImageGallery from "@/components/gallery/image_gallery";
import BodySidebarLayout from "@/components/layout/body_sidebar_layout";
import Sidebar from "@/components/sidebar/siddebar";
import TagTreeCard from "@/components/sidebar/widget/tree_card";
import DefaultSidebar from "@/components/sidebar/default_sidebar";

export default function Home() {
  return (
    <main>
      <BodySidebarLayout
        body={<ImageGallery />}
        sidebar={<DefaultSidebar />}
      />
    </main>
  )
}