import { useState } from 'react'
import MateriaCheckbox from './MateriaCheckbox'

function SemestreAccordion({ semestre, selectedMaterias, onToggleMateria, onToggleSemestre }) {
  const [open, setOpen] = useState(semestre.materias.length > 0)
  const isEmpty = semestre.materias.length === 0
  const allSelected = semestre.materias.length > 0
    && semestre.materias.every(m => selectedMaterias.has(m.codigo))
  const someSelected = semestre.materias.some(m => selectedMaterias.has(m.codigo))

  return (
    <div className={`semester-card ${isEmpty ? 'semester-empty' : ''}`}>
      <div
        className="semester-header"
        onClick={() => !isEmpty && setOpen(!open)}
      >
        <div className="semester-header-left">
          {!isEmpty && (
            <input
              type="checkbox"
              checked={allSelected}
              ref={el => {
                if (el) el.indeterminate = someSelected && !allSelected
              }}
              onChange={() => onToggleSemestre(semestre)}
              onClick={e => e.stopPropagation()}
              className="semester-checkbox"
            />
          )}
          <span className="semester-arrow">
            {isEmpty ? '' : open ? '\u25BC' : '\u25B6'}
          </span>
          <span className="semester-title">{semestre.nombre}</span>
        </div>
        <span className="semester-count">
          {isEmpty
            ? '0 materias — sin microcurrículos cargados'
            : `${semestre.materias.length} materia(s)`
          }
        </span>
      </div>

      {open && !isEmpty && (
        <div className="semester-body">
          {semestre.materias.map(materia => (
            <MateriaCheckbox
              key={materia.codigo + materia.archivo}
              materia={materia}
              checked={selectedMaterias.has(materia.codigo)}
              onToggle={() => onToggleMateria(materia.codigo)}
            />
          ))}
        </div>
      )}
    </div>
  )
}

export default SemestreAccordion
