function GenerateButton({ canGenerate, generating, selectedCount, onClick }) {
  return (
    <button
      className="btn btn-primary btn-generate"
      disabled={!canGenerate}
      onClick={onClick}
    >
      {generating
        ? 'Generando...'
        : `Generar documento (${selectedCount} materia${selectedCount !== 1 ? 's' : ''})`
      }
    </button>
  )
}

export default GenerateButton
