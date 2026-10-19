import { useState, useEffect, useCallback, useMemo } from 'react'
import axios from 'axios'
import StudentForm from './components/StudentForm'
import SearchBar from './components/SearchBar'
import SemestreColumn from './components/SemestreColumn'
import GenerateButton from './components/GenerateButton'
import ProgressIndicator from './components/ProgressIndicator'
import './App.css'

function App() {
  const [curriculos, setCurriculos] = useState([])
  const [selectedCurriculo, setSelectedCurriculo] = useState('')
  const [semestres, setSemestres] = useState([])
  const [totalMaterias, setTotalMaterias] = useState(0)
  const [selectedMaterias, setSelectedMaterias] = useState(new Set())
  const [nombre, setNombre] = useState('')
  const [codigo, setCodigo] = useState('')
  const [searchQuery, setSearchQuery] = useState('')
  const [loading, setLoading] = useState(false)
  const [generating, setGenerating] = useState(false)
  const [error, setError] = useState(null)
  const [success, setSuccess] = useState(null)

  // La búsqueda atenúa las materias que no coinciden sin mover la malla
  const matches = useCallback(materia => {
    const q = searchQuery.toLowerCase().trim()
    if (!q) return true
    return materia.nombre.toLowerCase().includes(q) || materia.codigo.toLowerCase().includes(q)
  }, [searchQuery])

  const matchCount = useMemo(() => {
    return semestres.reduce((acc, s) => acc + s.materias.filter(matches).length, 0)
  }, [semestres, matches])

  const semestresMarcados = useMemo(() => {
    return semestres
      .map(s => ({ numero: s.numero, n: s.materias.filter(m => selectedMaterias.has(m.codigo)).length }))
      .filter(s => s.n > 0)
  }, [semestres, selectedMaterias])

  const fetchCurriculos = useCallback(async () => {
    try {
      const { data } = await axios.get('/api/curriculos')
      setCurriculos(data.curriculos)
      if (data.curriculos.length > 0 && !selectedCurriculo) {
        setSelectedCurriculo(data.curriculos[0].nombre)
      }
    } catch {
      setError('No se pudieron cargar los pensums. Revisa que el servidor esté encendido.')
    }
  }, [selectedCurriculo])

  const fetchMaterias = useCallback(async () => {
    if (!selectedCurriculo) return
    setLoading(true)
    setError(null)
    try {
      const { data } = await axios.get('/api/microcurriculos', {
        params: { curriculo: selectedCurriculo }
      })
      setSemestres(data.semestres)
      setTotalMaterias(data.total_materias)
    } catch {
      setError('No se pudieron cargar las materias de este pensum.')
    } finally {
      setLoading(false)
    }
  }, [selectedCurriculo])

  useEffect(() => { fetchCurriculos() }, [fetchCurriculos])

  useEffect(() => {
    if (selectedCurriculo) {
      fetchMaterias()
      setSelectedMaterias(new Set())
      setSearchQuery('')
    }
  }, [selectedCurriculo, fetchMaterias])

  const handleRefresh = async () => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await axios.get('/api/microcurriculos/refresh', {
        params: { curriculo: selectedCurriculo }
      })
      setSemestres(data.semestres)
      setTotalMaterias(data.total_materias)
      if (data.archivos_renombrados?.length > 0) {
        setSuccess(`${data.archivos_renombrados.length} archivo(s) renombrado(s)`)
        setTimeout(() => setSuccess(null), 3000)
      }
    } catch {
      setError('No se pudieron actualizar las materias.')
    } finally {
      setLoading(false)
    }
  }

  const toggleMateria = (cod) => {
    setSelectedMaterias(prev => {
      const next = new Set(prev)
      next.has(cod) ? next.delete(cod) : next.add(cod)
      return next
    })
  }

  const toggleSemestre = (semestre) => {
    const codes = semestre.materias.map(m => m.codigo)
    const allSelected = codes.every(c => selectedMaterias.has(c))
    setSelectedMaterias(prev => {
      const next = new Set(prev)
      codes.forEach(c => allSelected ? next.delete(c) : next.add(c))
      return next
    })
  }

  const selectAll = () => {
    const allCodes = semestres.flatMap(s => s.materias.map(m => m.codigo))
    setSelectedMaterias(new Set(allCodes))
  }

  const deselectAll = () => setSelectedMaterias(new Set())

  const handleGenerar = async () => {
    setGenerating(true)
    setError(null)
    setSuccess(null)
    try {
      const response = await axios.post('/api/generar', {
        nombre: nombre.trim(),
        codigo: codigo.trim(),
        materias: Array.from(selectedMaterias),
        curriculo: selectedCurriculo,
      }, { responseType: 'blob' })

      const url = window.URL.createObjectURL(new Blob([response.data]))
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', `${nombre.trim().replace(/\s+/g, '_')}_Microcurriculos.pdf`)
      document.body.appendChild(link)
      link.click()
      link.remove()
      window.URL.revokeObjectURL(url)

      setSuccess('PDF generado. Revisa tu carpeta de descargas.')
      setTimeout(() => setSuccess(null), 5000)
    } catch (err) {
      // con responseType 'blob' el detalle del backend llega como Blob
      const data = err.response?.data
      const detail = data instanceof Blob
        ? await data.text().then(t => JSON.parse(t).detail).catch(() => null)
        : data?.detail
      setError(detail || 'No se pudo generar el PDF.')
    } finally {
      setGenerating(false)
    }
  }

  const faltante = !nombre.trim()
    ? 'Escribe el nombre del estudiante.'
    : !codigo.trim()
      ? 'Escribe el código estudiantil.'
      : selectedMaterias.size === 0
        ? 'Marca al menos una materia en la malla.'
        : null

  const canGenerate = selectedMaterias.size > 0
    && nombre.trim().length > 0
    && codigo.trim().length > 0
    && !generating

  return (
    <div className="app">
      <header className="topbar">
        <div className="topbar-inner">
          <div className="brand">
            <span className="brand-mark" aria-hidden="true">UFPS</span>
            <div>
              <p className="brand-programa">Ingeniería de Sistemas</p>
              <h1 className="brand-titulo">Microcurrículos</h1>
            </div>
          </div>
          <button
            type="button"
            className="btn-topbar"
            onClick={handleRefresh}
            disabled={loading}
          >
            <span className={loading ? 'spin' : ''} aria-hidden="true">&#x21bb;</span>
            Actualizar materias
          </button>
        </div>
      </header>

      <main className="workbench">
        <aside className="rail">
          <section className="panel">
            <h2 className="panel-titulo">Pensum</h2>
            <div className="pensums">
              {curriculos.map(c => (
                <button
                  key={c.nombre}
                  type="button"
                  className={`pensum ${selectedCurriculo === c.nombre ? 'pensum-on' : ''}`}
                  aria-pressed={selectedCurriculo === c.nombre}
                  onClick={() => setSelectedCurriculo(c.nombre)}
                >
                  <span className="pensum-codigo">{c.nombre.replace('Curriculo ', '')}</span>
                  <span className="pensum-estado">
                    {c.plantilla_presente ? 'Plantilla lista' : 'Falta la plantilla'}
                  </span>
                </button>
              ))}
              <div className="pensum pensum-pronto" aria-disabled="true">
                <span className="pensum-codigo">Nuevos pensums</span>
                <span className="pensum-estado">Aquí se podrán agregar más adelante</span>
                <span className="pronto">Próximamente</span>
              </div>
            </div>
          </section>

          <section className="panel">
            <h2 className="panel-titulo">Estudiante</h2>
            <StudentForm
              nombre={nombre}
              setNombre={setNombre}
              codigo={codigo}
              setCodigo={setCodigo}
            />
          </section>

          <section className="panel panel-resumen">
            <p className="resumen-total">
              <strong>{selectedMaterias.size}</strong>
              <span>de {totalMaterias} materias marcadas</span>
            </p>
            {semestresMarcados.length > 0 && (
              <ul className="resumen-semestres" aria-label="Materias marcadas por semestre">
                {semestresMarcados.map(s => (
                  <li key={s.numero}>
                    <span>{['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'][s.numero - 1]}</span>
                    {s.n}
                  </li>
                ))}
              </ul>
            )}

            <GenerateButton
              canGenerate={canGenerate}
              generating={generating}
              selectedCount={selectedMaterias.size}
              onClick={handleGenerar}
            />
            {faltante && !generating && <p className="resumen-falta">{faltante}</p>}
            {generating && (
              <ProgressIndicator message="Convirtiendo y uniendo los documentos. Puede tardar unos minutos." />
            )}

            {error && (
              <div className="aviso aviso-error" role="alert">
                <p>{error}</p>
                <button type="button" className="aviso-cerrar" onClick={() => setError(null)} aria-label="Cerrar aviso">&times;</button>
              </div>
            )}
            {success && (
              <div className="aviso aviso-ok" role="status">
                <p>{success}</p>
                <button type="button" className="aviso-cerrar" onClick={() => setSuccess(null)} aria-label="Cerrar aviso">&times;</button>
              </div>
            )}
          </section>
        </aside>

        <section className="board">
          <div className="board-head">
            <div>
              <h2 className="board-titulo">Plan de estudios {selectedCurriculo.replace('Curriculo ', '')}</h2>
              <p className="board-ayuda">Toca una materia para incluirla en el documento.</p>
            </div>
            <div className="board-tools">
              <SearchBar
                value={searchQuery}
                onChange={setSearchQuery}
                placeholder="Buscar por nombre o código"
                resultCount={searchQuery ? matchCount : null}
              />
              <button type="button" className="btn-linea" onClick={selectAll} disabled={loading}>
                Marcar todas
              </button>
              <button type="button" className="btn-linea" onClick={deselectAll} disabled={loading || selectedMaterias.size === 0}>
                Limpiar
              </button>
            </div>
          </div>

          <div className="importar-pronto" aria-disabled="true">
            <svg viewBox="0 0 24 24" className="importar-icono" aria-hidden="true">
              <rect x="3" y="5" width="18" height="14" rx="2" />
              <circle cx="9" cy="10" r="2" />
              <path d="M21 16l-5-5-8 8" />
            </svg>
            <div className="importar-texto">
              <p className="importar-titulo">Seleccionar desde una imagen <span className="pronto">Próximamente</span></p>
              <p>Sube la foto del certificado de notas, elige el pensum y las materias se marcarán solas.</p>
            </div>
            <button type="button" className="btn-linea" disabled>Subir imagen</button>
          </div>

          {loading ? (
            <div className="board-cargando">
              <ProgressIndicator message="Cargando materias…" />
            </div>
          ) : (
            <div className="malla">
              {semestres.map(semestre => (
                <SemestreColumn
                  key={semestre.numero}
                  semestre={semestre}
                  selectedMaterias={selectedMaterias}
                  matches={matches}
                  onToggleMateria={toggleMateria}
                  onToggleSemestre={toggleSemestre}
                />
              ))}
            </div>
          )}
          {!loading && searchQuery && matchCount === 0 && (
            <p className="board-vacio">Ninguna materia coincide con &ldquo;{searchQuery}&rdquo;. Prueba con el código o con otra palabra del nombre.</p>
          )}
        </section>
      </main>
    </div>
  )
}

export default App
