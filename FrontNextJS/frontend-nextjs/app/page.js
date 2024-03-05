import Image from "next/image";
import styles from "./page.module.css";
import "bootstrap/dist/css/bootstrap.min.css";
import ImageGallery from "@/components/gallery/image_gallery";
import BodySidebarLayout from "@/components/layout/body_sidebar_layout";
import Sidebar from "@/components/sidebar/siddebar";
import TreeCard from "@/components/sidebar/widget/tree_card";
import DeafultSidebar from "@/components/sidebar/default_sidebar";

export default function Home() {
  // const sidebar = <DeafultSidebar />
  return (
    <BodySidebarLayout
      body={<ImageGallery />}
      sidebar={<DeafultSidebar />}
    />
  )
}