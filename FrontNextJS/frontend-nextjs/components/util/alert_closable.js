'use client'

export default function AlertClosable({ type='info', text='这是一个标签！', strong='注意！' }) {
    return (
        <div className={`alert alert-${type}`} style={{"borderRadius": '10px'}}>
            <strong>{strong}</strong>
            {text}
        </div>
    )
}