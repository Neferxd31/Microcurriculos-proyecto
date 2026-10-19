import MateriaCheckbox from './MateriaCheckbox'

const ROMANOS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

function SemestreColumn({ semestre, selectedMaterias, matches, onToggleMateria, onToggleSemestre }) {
  const total = semestre.materias.length
  const marcadas = semestre.materias.filter(m => selectedMaterias.has(m.codigo)).length
  const completo = total > 0 && marcadas === total

  return (
    <section className="semestre" aria-label={semestre.nombre}>
      <header className="semestre-head">
        <span className="semestre-numero">{ROMANOS[semestre.numero - 1]}</span>
        <div className="semestre-meta">
          <span>{total === 0 ? 'Sin materias' : `${marcadas} de ${total}`}</span>
          {total > 0 && (
            <button
              type="button"
              className="semestre-toggle"
              onClick={() => onToggleSemestre(semestre)}
            >
              {completo ? 'Quitar todas' : 'Marcar todas'}
            </button>
          )}
        </div>
      </header>

      {total === 0
        ? <p className="semestre-vacio">No hay microcurrículos cargados para este semestre.</p>
        : (
          <ul className="semestre-materias">
            {semestre.materias.map(materia => (
              <li key={materia.codigo + materia.archivo}>
                <MateriaCheckbox
                  materia={materia}
                  checked={selectedMaterias.has(materia.codigo)}
                  dimmed={!matches(materia)}
                  onToggle={() => onToggleMateria(materia.codigo)}
                />
              </li>
            ))}
          </ul>
        )}
    </section>
  )
}

export default SemestreColumn
