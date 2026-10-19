const CONECTORES = new Set(['de', 'del', 'la', 'el', 'las', 'los', 'y', 'a', 'en', 'para'])
const ROMANO = /^(i{1,3}|iv|vi{0,3}|ix|x)$/i

// El nombre llega desde el archivo (p. ej. "Microcurriciulo Comunicacion Ii"); se limpia solo para mostrarlo
function nombreLegible(nombre) {
  return nombre
    .replace(/microcurr\S*/gi, '')
    .replace(/-ra\b/gi, '')
    .replace(/\b\d{7}(-\w)?\b/g, '')
    .split(/\s+/)
    .filter(Boolean)
    .map((palabra, i) => {
      if (ROMANO.test(palabra)) return palabra.toUpperCase()
      if (i > 0 && CONECTORES.has(palabra.toLowerCase())) return palabra.toLowerCase()
      return palabra
    })
    .join(' ')
}

function MateriaCheckbox({ materia, checked, dimmed, onToggle }) {
  const classes = ['materia', checked && 'materia-on', dimmed && 'materia-dim'].filter(Boolean).join(' ')

  return (
    <label className={classes}>
      <input
        type="checkbox"
        checked={checked}
        onChange={onToggle}
        className="materia-input"
      />
      <span className="materia-codigo">{materia.codigo}</span>
      <span className="materia-nombre">{nombreLegible(materia.nombre)}</span>
      {!materia.formato_valido && (
        <span className="materia-alerta" title="El nombre del archivo no sigue el formato código_Nombre.docx">
          Revisar archivo
        </span>
      )}
    </label>
  )
}

export default MateriaCheckbox
