import BiIcon from "../util/bi_icon";
import Sidebar from "./siddebar";
import Card from "./widget/card";
import TreeCard from "./widget/tree_card";
import TreeViewAsync from "../tree/tree_view_async";

export default function DefaultSidebar({
    children
}) {
    const folder_card = <TreeCard
        title={"文件夹列表"}
        icon={<BiIcon bicode="folder" />}
        rootUrl={"folders/roots"}
        nodeUrl={'folders'}
    />

    const tag_card = <TreeCard
    //title='标签列表'
    //icon = <BiIcon bicode="tags" />
    //rootUrl = '/tags/roots'
    //nodeUrl = '/tags'
    />

    const tag_rootUrl = 'tags/roots'
    const tag_nodeUrl = "tags"

    const folder_rootUrl = 'folders/roots'
    const folder_nodeUrl = "folders"

    const folder_temp = <Card
        title={'文件夹列表'}
        icon={<BiIcon bicode="folder-symlink" />}
        content={
            <div>
                <TreeViewAsync
                    rootUrl={folder_rootUrl}
                    nodeUrl={folder_nodeUrl}
                    icon={<BiIcon bicode="folder" />}
                />
            </div>
        }
    />

    const tag_temp = <Card
        title={'标签列表'}
        icon={<BiIcon bicode="tags" />}
        content={
            <div>
                <TreeViewAsync
                    rootUrl={tag_rootUrl}
                    nodeUrl={tag_nodeUrl}
                    icon={<BiIcon bicode="tag" />}
                />
            </div>
        }
    />



    return (
        <Sidebar
            //folder_tree={folder_card}
            tag_tree={tag_temp}
            folder_tree={folder_temp}
        >
            {children}
        </Sidebar>
    )
}