import AlertClosable from "@/components/util/alert_closable"

export default function NotFoundPage() {
    return (
        <div>
            <AlertClosable
                type='info'
                strong="404 Not Found！"
                text="我们找不到这个页面，或许你输入了错误的地址。你也可以查看右侧的标签树以及文章列表来查看图片。"
            />
        </div>
    )
}