import Image from "next/image";
import { site_title } from "@/app/config/config";

export default function Home() {
  return (

    <h1>这是一个示例页面：{ site_title }</h1>


  );
}
