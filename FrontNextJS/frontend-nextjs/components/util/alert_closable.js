'use client'

export default function AlertClosable({ type, text }) {
    return (
        <div class={`alert alert-${type}`} style={{"borderRadius": '10px'}}>
            <strong>这里是侧边栏。</strong>
            这里应该会出现有关图片的信息以及标签、文件夹列表。当前这里没有任何信息，<strong>你应该向网站运营人员反馈这个问题！</strong>
        </div>
    )
}