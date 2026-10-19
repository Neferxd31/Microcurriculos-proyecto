function GenerateButton({ canGenerate, generating, selectedCount, onClick }) {
  const materias = `${selectedCount} materia${selectedCount !== 1 ? 's' : ''}`

  return (
    <button
      type="button"
      className="btn-generar"
      disabled={!canGenerate}
      onClick={onClick}
    >
      {generating ? 'Generando PDF…' : `Generar PDF con ${materias}`}
    </button>
  )
}

export default GenerateButton
