function StudentForm({ nombre, setNombre, codigo, setCodigo }) {
  return (
    <div className="form-row">
      <div className="form-group">
        <label htmlFor="nombre">Nombre completo</label>
        <input
          id="nombre"
          type="text"
          placeholder="Ej: Juan Perez"
          value={nombre}
          onChange={e => setNombre(e.target.value)}
        />
      </div>
      <div className="form-group">
        <label htmlFor="codigo">Codigo estudiantil</label>
        <input
          id="codigo"
          type="text"
          placeholder="Ej: 1151234"
          value={codigo}
          onChange={e => setCodigo(e.target.value)}
        />
      </div>
    </div>
  )
}

export default StudentForm
