// PDF VIEWER COMPONENT

import './PdfViewer.css';

import React, { useState } from 'react';
import { Document, Page } from 'react-pdf';

export default function PdfViewer({ pdf }) {

  const [loading, setLoading] = useState(true);

  const handleLoadSuccess = () => {
    console.log('PDF loaded successfully');
    setLoading(false);
  };

  const handleLoadError = (error) => {
    console.error('Error loading PDF:', error);
    setLoading(false);
  };

  return (
    <div className="pdf-viewer">
      {loading && <p>Loading...</p>}
      <Document file={pdf} onLoadSuccess={handleLoadSuccess} onLoadError={handleLoadError}>
        <Page pageNumber={1} />
      </Document>
    </div>
  );
}