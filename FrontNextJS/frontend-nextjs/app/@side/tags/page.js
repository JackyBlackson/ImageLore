import AlertStatic from "@/components/util/alert_static"

export default function TagsPageSidebar({ }) {
  return (
    <AlertStatic
      type='info'
      strong='这是标签页面。'
      text='在左侧将展示本网站所有标签的结构，包括彼此之间的联系。你可以点击左侧的标签来浏览标签详情，或者浏览下方的文件夹和标签树来浏览其他页面'
    />
  )
}