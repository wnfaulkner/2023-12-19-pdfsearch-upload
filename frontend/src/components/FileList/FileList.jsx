// FILE LIST COMPONENT

import './FileList.css'

import React, {useState,useEffect} from 'react'

import FileCard from '../FileCard/FileCard.jsx'
import PdfViewer from '../PdfViewer/PdfViewer.jsx'

export default function FileList({ fileList }) {

  const [selectedPdf, setSelectedPdf] = useState(null);

  const openPdfViewer = (pdfPath) => {
    setSelectedPdf(pdfPath);
    // console.log('setSelectedPdf ran!')
  };

  return(
    <div id="file-list">
      {fileList.map((file, idx) => (
        <FileCard file={file} key={idx} openPdfViewer={ openPdfViewer } />
      ))}
      {selectedPdf && <PdfViewer pdf={selectedPdf} />}
    </div>
  )
}
