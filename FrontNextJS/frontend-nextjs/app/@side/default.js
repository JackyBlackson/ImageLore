import AlertClosable from "@/components/util/alert_closable";

export default function Sidebar({ }) {
    return (
        <AlertClosable
            type='danger'
            strong="你来到了令人意外的地址。"
            text="我们并不知道这个地址的含义。也许你可以点击下面的文件夹和标签来浏览其他的图片。"
        />
    )
}