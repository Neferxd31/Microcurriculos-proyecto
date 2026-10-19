function SearchBar({ value, onChange, placeholder, resultCount }) {
  return (
    <div className="search">
      <svg className="search-icon" viewBox="0 0 20 20" aria-hidden="true">
        <circle cx="8.5" cy="8.5" r="5.5" />
        <path d="M13 13l4 4" />
      </svg>
      <input
        type="search"
        className="search-input"
        placeholder={placeholder}
        aria-label="Buscar materia"
        value={value}
        onChange={e => onChange(e.target.value)}
      />
      {value && resultCount !== null && (
        <span className="search-count">{resultCount} {resultCount === 1 ? 'coincide' : 'coinciden'}</span>
      )}
    </div>
  )
}

export default SearchBar
