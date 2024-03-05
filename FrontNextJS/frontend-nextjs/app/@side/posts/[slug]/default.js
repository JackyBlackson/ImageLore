import AlertClosable from "@/components/util/alert_closable";
import BiIcon from "@/components/util/bi_icon";
import Card from "@/components/sidebar/widget/card";
import AlertStatic from "@/components/util/alert_static";

export default function Sidebar({ }) {
    const title = '图片详细信息'
    const icon = <BiIcon bicode="info-circle" />
    const content = <AlertStatic
        type='danger'
        strong='你查找的图片不存在！'
        text='或许你可以点击下面的文件夹或者标签来重新寻找一张图片来查看？'
    />

    return (
        <Card
            title={title}
            icon={icon}
            content={content}
        />
    )
}