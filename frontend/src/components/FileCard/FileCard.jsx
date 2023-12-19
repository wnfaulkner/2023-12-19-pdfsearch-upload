// FILE CARD COMPONENT

export default function FileCard({ file, idx }) {
  return (
    <div className="file-card">
      <div>
        <p className="file-id">Id: {file.id}</p>
        <p className="file-location">Location: {file.pdf}</p>
      </div>
    </div>
  )
}