'use client'

import ImageGallery from "@/components/gallery/image_gallery"
import "bootstrap/dist/css/bootstrap.min.css";
import AlertStatic from "@/components/util/alert_static";
import SearchInput from "@/components/serch/search_input";

export default function SearchPage({ params }) {
  const expression = decodeURIComponent(params.slug);
  if (expression) {
    console.log('expr: ', expression)
    return (
      <ImageGallery apiUrl={`posts/images/search`} searchParam={`expr=${encodeURIComponent(expression)}`} />
    )
  } else {
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
}