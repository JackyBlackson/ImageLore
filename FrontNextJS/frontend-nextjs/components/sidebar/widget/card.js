import BiIcon from "@/components/util/bi_icon"

export default function Card({
    icon = <BiIcon bicode="card-heading" />,
    content = <p>这是一个侧边栏卡片！</p>,
    title = '侧边栏卡片'
}) {
    return (
        <div className="card pr-2 sidebar_card" style={{borderRadius: '10px'}}>
            <h5 className="card-header text-white p-3" style={{backgroundColor: "indigo", borderRadius: '10px'}}>
                {icon}
                <span>{title}</span>
            </h5>
            <div className="card-body" style={{paddingRight: "10px"}}>
                {content}
            </div>
        </div>
    )
}