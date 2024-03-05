import AlertClosable from "@/components/util/alert_closable"
import "bootstrap/dist/css/bootstrap.min.css";
import DetailBigImage from "@/components/gallery/widget/detail_big_image";
import { backend_root } from "@/app/config/global";
import CardImageDetail from "@/components/sidebar/card_image_detail";

export default function Sidebar({ params }) {
    const id = params.slug;
    return (
        <CardImageDetail
            imageId={id}
        />
    )
}