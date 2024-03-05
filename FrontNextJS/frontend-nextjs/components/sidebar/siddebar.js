'use client'
import SearchBar from "./widget/search_bar"
import AlertStatic from "../util/alert_static"

export default function Sidebar({ folder_tree, tag_tree, children }) {
    return(
        <div>
            <SearchBar />
            {children}
            { 
                folder_tree ? folder_tree : <AlertStatic type={"danger"}/>
            }
            { 
                tag_tree ? tag_tree : <AlertStatic type={"danger"}/>
            }
            
        </div>
    )
}