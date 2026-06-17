function ProgressIndicator({ message }) {
  return (
    <div className="progress-indicator">
      <div className="spinner" />
      <span>{message}</span>
    </div>
  )
}

export default ProgressIndicator
