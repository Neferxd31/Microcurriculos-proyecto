function MateriaCheckbox({ materia, checked, onToggle }) {
  return (
    <label className={`materia-row ${checked ? 'materia-selected' : ''}`}>
      <input
        type="checkbox"
        checked={checked}
        onChange={onToggle}
        className="materia-checkbox"
      />
      <span className="materia-code">{materia.codigo}</span>
      <span className="materia-separator">—</span>
      <span className="materia-name">{materia.nombre}</span>
      {!materia.formato_valido && (
        <span className="materia-warning" title="Nombre de archivo no sigue el formato estándar">
          !!
        </span>
      )}
    </label>
  )
}

export default MateriaCheckbox
