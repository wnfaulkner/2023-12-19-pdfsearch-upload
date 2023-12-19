// FILE CARD COMPONENT

import './FileCard.css'

import pdfIcon from '../../images/pdf-icon.png'

export default function FileCard({ file, idx }) {

  const openPdf = () => {
    console.log('Open PDF clicked!')
    // Replace 'path/to/your/pdf.pdf' with the actual path to your PDF file
    // const pdfUrl = 'path/to/your/pdf.pdf';
    
    // Open the PDF in a new tab or window
    // window.open(pdfUrl, '_blank');
  };

  return (
    <div className="file-card">
        <div className="file-card-component">
          <img
            src={pdfIcon}
            alt="PDF Icon"
            style={{ cursor: 'pointer' }}
            onClick={openPdf}
            className='file-icon'
          />
        </div>
        <div className="file-card-component">
          <p className="file-id">Id: {file.id}</p>
        </div>
        <div className="file-card-component">
          <p className="file-location">Location: {file.pdf}</p>
        </div>
    </div>
  )
}