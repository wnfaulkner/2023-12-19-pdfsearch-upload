// FILE LIST COMPONENT

import './FileList.css'

import FileCard from '../FileCard/FileCard.jsx'

export default function FileList({ fileList }) {
  return(
    <div id="file-list">
      {fileList.map((file, idx) => (
        <FileCard file={file} idx={idx} />
      ))}
    </div>
  )
}
