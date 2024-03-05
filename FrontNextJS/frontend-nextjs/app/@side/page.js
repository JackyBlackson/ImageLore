import AlertClosable from "@/components/util/alert_closable";
import { site_title } from "../config/global";



export default function Sidebar({ }) {
    return (
        <AlertClosable
            type='info'
            strong={`欢迎来${site_title}！到这里是侧边栏。`}
            text="你可以在这里查看图片的文件夹以及标签分布。你可以点击文件夹或者标签来浏览所有带有这些标签的图片。在详情页中，这里也会展示所选项目的详细信息以及其他选项。"
        />
    )
}