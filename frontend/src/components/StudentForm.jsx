function StudentForm({ nombre, setNombre, codigo, setCodigo }) {
  return (
    <div className="form">
      <label className="field">
        <span>Nombre completo</span>
        <input
          type="text"
          placeholder="Como aparece en el certificado"
          autoComplete="off"
          value={nombre}
          onChange={e => setNombre(e.target.value)}
        />
      </label>
      <label className="field">
        <span>Código estudiantil</span>
        <input
          type="text"
          inputMode="numeric"
          placeholder="1152260"
          autoComplete="off"
          value={codigo}
          onChange={e => setCodigo(e.target.value)}
        />
      </label>
    </div>
  )
}

export default StudentForm
