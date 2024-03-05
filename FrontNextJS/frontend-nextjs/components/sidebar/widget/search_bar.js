'use client'

export default function SearchBar() {
  return (
    <form className="d-flex mb-3">
      <input className="form-control me-2 flex-grow-1" type="text" placeholder="Search" />
      <button className="btn btn-primary" type="button">
      <i className="bi bi-search"></i>
      </button>
    </form>
  )
}