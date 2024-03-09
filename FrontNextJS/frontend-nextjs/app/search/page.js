'use client'

import ImageGallery from "@/components/gallery/image_gallery"
import "bootstrap/dist/css/bootstrap.min.css";
import DetailBigImage from "@/components/gallery/widget/detail_big_image";
import { backend_root } from "@/app/config/global";
import { site_title } from "@/app/config/global";
import AlertStatic from "@/components/util/alert_static";
import SearchInput from "@/components/serch/search_input";

export default function SearchPage() {
    return (
      <>
        <SearchInput />
        <AlertStatic
          type='info'
          strong='你没有输入查询目标表达式！'
          text='你应该输入！'
        />
      </>
    )

}