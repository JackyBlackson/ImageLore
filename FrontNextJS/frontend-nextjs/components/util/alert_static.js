'use client'

export default function AlertStatic({ type, text, strong }) {
    return (
        <div className={`alert alert-${type}`} style={{"borderRadius": '10px'}}>
            <strong>{strong}</strong>
            {text}
        </div>
    )
}