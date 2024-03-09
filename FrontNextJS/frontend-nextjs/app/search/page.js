'use client'

import "bootstrap/dist/css/bootstrap.min.css";
import AlertStatic from "@/components/util/alert_static";
import SearchInput from "@/components/serch/search_input";

export default function SearchPage() {
  return (
    <>
      <SearchInput />
      <AlertStatic
        type='info'
        strong= {<p>这里是搜索页面！你可以输入表达式来进行复杂的检索。以下是帮助（提供的示例值仅作为例子，不代表本网站的真实数据）：</p>}
        text={
          <p>
            <ol>
              <p>
                <li>

                  表达式中的值表示的是某个范围内的图片的集合。你可以用这些方法来获得值：
                  <ul>
                    <li><strong>“#[标签]”</strong>用来代表这个标签（及其子标签）的所有图片集合，例如：<code>#古建筑</code></li>
                    <li><strong>“@[用户名]”</strong>用来代表这个用户上传的所有图片集合，例如：<code>@Chuanwise</code></li>
                    <li><strong>“/[文件夹名]”</strong>用来代表这个文件夹（及其子文件夹）的所有图片集合，例如：<code>/智化寺</code></li>
                    <li><strong>“*”</strong>用来代表这个本网站拥有的所有的图片集合，例如：<code>*</code></li>
                  </ul>

                </li>
              </p>
              <p>
                <li>
                  表达式的运算符表达了两个图片集合的运算，其运算规则和一般集合运算是相同的：
                  <ul>
                    <li><strong>“a & b”</strong>得到的是集合a与b的交集，仅包括同时在集合a和集合b中的图片，例如：<code>#古建筑 & @Chuanwise</code></li>
                    <li><strong>“a + b”</strong>得到的是集合a与b的并集，包括了所有出现在集合a或集合b的图片，例如：<code>/智化寺 + @Chuanwise</code></li>
                    <li><strong>“a | b”</strong>得到的是集合a与b的并集，与“a + b”的含义和结果均是相同的，例如：<code>/智化寺 + @Chuanwise</code></li>
                    <li><strong>“a - b”</strong>得到的是集合a与b的差集，包括了所有出现在集合a但不出现在集合b的图片，例如：<code>/智化寺 - @Chuanwise</code></li>
                    <li><strong>“a b”</strong>，也就是把两个值写在一起，中间没有运算符也是合法的，我们会在中间添加一个“&”运算符，等价于“a & b”，例如：<code>#古建筑 #老照片</code>等价于<code>#古建筑 & #老照片</code></li>
                  </ul>
                </li>
              </p>
              <p>
                <li>
                  当然你还可以使用“()”【英文括号】或者“（）”【中文括号】来提高表达式的优先级，但需要注意括号必须闭合且配对：
                  <ul>
                    <li><strong>“* - (a & b)”</strong>表示先运算“a & b”，然后将得到的值和“*”作差集</li>
                    <li><strong>“（a - b) - c”</strong>，全角（中文）半角（英文）括号是等价的，可以混合使用，也可以全部用某一种</li>
                    <li><strong>“（a | b”</strong>不配对的括号是非法的，进行搜索会报告错误</li>
                    <li><strong>“a - b”</strong>得到的是集合a与b的差集，包括了所有出现在集合a但不出现在集合b的图片，例如：<code>/智化寺 - @Chuanwise</code></li>
                  </ul>
                </li>
              </p>
              <p>
                <li>
                  还有一些其他你应该知道的搜索小技巧：
                  <ul>
                  <li><strong>“a-b-c ≡ a - b - c”</strong>，表达式中，运算符和值之间可以出现任意多的空格，这不会影响表达式的检索</li>
                    <li><strong>“a & (* - b) ≡ a - b”</strong>集合运算是可以化简的；虽然不会产生什么问题，但是化简表达式可以提高检索的速度</li>
                  </ul>
                </li>
              </p>
            </ol>
          </p>
        }
      />
    </>
  )

}