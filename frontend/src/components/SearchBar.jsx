function SearchBar({ value, onChange, placeholder, resultCount }) {
  return (
    <div className="search-bar">
      <span className="search-icon">&#x1F50D;</span>
      <input
        type="text"
        className="search-input"
        placeholder={placeholder}
        value={value}
        onChange={e => onChange(e.target.value)}
      />
      {value && (
        <>
          {resultCount !== null && (
            <span className="search-count">{resultCount} resultado(s)</span>
          )}
          <button className="search-clear" onClick={() => onChange('')}>&#x00d7;</button>
        </>
      )}
    </div>
  )
}

export default SearchBar
