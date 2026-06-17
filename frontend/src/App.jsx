import { useState, useEffect, useCallback, useMemo } from 'react'
import axios from 'axios'
import StudentForm from './components/StudentForm'
import SearchBar from './components/SearchBar'
import SemestreAccordion from './components/SemestreAccordion'
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

  // Filtrar semestres por búsqueda
  const filteredSemestres = useMemo(() => {
    if (!searchQuery.trim()) return semestres
    const q = searchQuery.toLowerCase().trim()
    return semestres
      .map(sem => ({
        ...sem,
        materias: sem.materias.filter(m =>
          m.nombre.toLowerCase().includes(q)
          || m.codigo.toLowerCase().includes(q)
        ),
      }))
      .filter(sem => sem.materias.length > 0)
  }, [semestres, searchQuery])

  const filteredCount = useMemo(() => {
    return filteredSemestres.reduce((acc, s) => acc + s.materias.length, 0)
  }, [filteredSemestres])

  const fetchCurriculos = useCallback(async () => {
    try {
      const { data } = await axios.get('/api/curriculos')
      setCurriculos(data.curriculos)
      if (data.curriculos.length > 0 && !selectedCurriculo) {
        setSelectedCurriculo(data.curriculos[0].nombre)
      }
    } catch {
      setError('Error cargando curriculos')
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
      setError('Error cargando microcurriculos')
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
      setError('Error refrescando microcurriculos')
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

      setSuccess('Documento generado y descargado exitosamente')
      setTimeout(() => setSuccess(null), 5000)
    } catch (err) {
      setError(err.response?.data?.detail || 'Error generando documento')
    } finally {
      setGenerating(false)
    }
  }

  const canGenerate = selectedMaterias.size > 0
    && nombre.trim().length > 0
    && codigo.trim().length > 0
    && !generating

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <div className="header-brand">
            <div className="brand-icon">UFPS</div>
            <div>
              <h1>Generador de Microcurriculos</h1>
              <p className="subtitle">Programa de Ingenieria de Sistemas</p>
            </div>
          </div>
          <button
            className="btn btn-icon"
            onClick={handleRefresh}
            disabled={loading}
            title="Refrescar materias"
          >
            <span className={`refresh-icon ${loading ? 'spin' : ''}`}>&#x21bb;</span>
          </button>
        </div>
      </header>

      <main className="app-main">
        {/* Alertas */}
        {error && (
          <div className="alert alert-error">
            <span>&#x2715; {error}</span>
            <button className="alert-close" onClick={() => setError(null)}>&#x00d7;</button>
          </div>
        )}
        {success && (
          <div className="alert alert-success">
            <span>&#x2713; {success}</span>
            <button className="alert-close" onClick={() => setSuccess(null)}>&#x00d7;</button>
          </div>
        )}

        {/* Selector de curriculo */}
        {curriculos.length > 0 && (
          <section className="section curriculo-section">
            <h2 className="section-title">Curriculo</h2>
            <div className="curriculo-grid">
              {curriculos.map(c => (
                <button
                  key={c.nombre}
                  className={`curriculo-card ${selectedCurriculo === c.nombre ? 'curriculo-active' : ''}`}
                  onClick={() => setSelectedCurriculo(c.nombre)}
                >
                  <span className="curriculo-code">{c.nombre.replace('Curriculo ', '')}</span>
                  <span className="curriculo-label">{c.nombre}</span>
                  <span className={`curriculo-badge ${c.plantilla_presente ? 'badge-ok' : 'badge-warn'}`}>
                    {c.plantilla_presente ? 'Listo' : 'Sin plantilla'}
                  </span>
                </button>
              ))}
            </div>
          </section>
        )}

        {/* Datos del estudiante */}
        <section className="section">
          <h2 className="section-title">Datos del Estudiante</h2>
          <StudentForm
            nombre={nombre}
            setNombre={setNombre}
            codigo={codigo}
            setCodigo={setCodigo}
          />
        </section>

        {/* Materias */}
        <section className="section">
          <div className="section-header-row">
            <h2 className="section-title">Materias</h2>
            <div className="toolbar-actions">
              <button className="btn btn-sm btn-outline" onClick={selectAll} disabled={loading}>
                Seleccionar todas
              </button>
              <button className="btn btn-sm btn-outline" onClick={deselectAll} disabled={loading}>
                Deseleccionar
              </button>
            </div>
          </div>

          <SearchBar
            value={searchQuery}
            onChange={setSearchQuery}
            placeholder="Buscar por nombre o codigo..."
            resultCount={searchQuery ? filteredCount : null}
          />

          {/* Barra de progreso de seleccion */}
          <div className="selection-bar">
            <div className="selection-track">
              <div
                className="selection-fill"
                style={{ width: totalMaterias ? `${(selectedMaterias.size / totalMaterias) * 100}%` : '0%' }}
              />
            </div>
            <span className="selection-text">
              <strong>{selectedMaterias.size}</strong> / {totalMaterias} seleccionadas
            </span>
          </div>

          {loading ? (
            <div className="loading-container">
              <ProgressIndicator message="Cargando materias..." />
            </div>
          ) : (
            <div className="semestres-list">
              {filteredSemestres.length === 0 && searchQuery ? (
                <div className="empty-state">
                  No se encontraron materias para &ldquo;{searchQuery}&rdquo;
                </div>
              ) : (
                filteredSemestres.map(semestre => (
                  <SemestreAccordion
                    key={semestre.numero}
                    semestre={semestre}
                    selectedMaterias={selectedMaterias}
                    onToggleMateria={toggleMateria}
                    onToggleSemestre={toggleSemestre}
                  />
                ))
              )}
            </div>
          )}
        </section>

        {/* Boton generar */}
        <div className="generate-section">
          <GenerateButton
            canGenerate={canGenerate}
            generating={generating}
            selectedCount={selectedMaterias.size}
            onClick={handleGenerar}
          />
          {generating && (
            <ProgressIndicator message="Generando PDF... esto puede tardar unos minutos" />
          )}
        </div>
      </main>

      <footer className="app-footer">
        <p>UFPS &mdash; Programa de Ingenieria de Sistemas</p>
      </footer>
    </div>
  )
}

export default App
