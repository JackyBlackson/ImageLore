import "bootstrap/dist/css/bootstrap.min.css";
import CardImageDetail from "@/components/sidebar/card_image_detail";

export default function Sidebar({ params }) {
    const id = params.slug;
    return (
        <CardImageDetail
            imageId={id}
        />
    )
}