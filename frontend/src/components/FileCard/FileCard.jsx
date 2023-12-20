// FileCard.jsx

import './FileCard.css';
import pdfIcon from '../../images/pdf-icon.png';
import React from 'react';

export default function FileCard({ file, idx, openPdfViewer }) {
  const openPdf = () => {
    // console.log('Open PDF clicked!');
    openPdfViewer(file.pdf);
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
  );
}
