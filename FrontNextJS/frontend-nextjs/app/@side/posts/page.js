import AlertClosable from "@/components/util/alert_closable";
import { site_title } from "@/app/config/global";

export default function Sidebar({ }) {
    return (
        <AlertClosable
            type='info'
            strong={`这里是${site_title}的图片库页面。`}
            text="将来这里会显示本页面图片包含的所有标签，但目前这里并没有内容……"
        />
    )
}