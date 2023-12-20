// PDF VIEWER COMPONENT

import './PdfViewer.css';

import React, { useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';

// pdfjs.GlobalWorkerOptions.workerSrc = new URL(
//   'pdfjs-dist/build/pdf.worker.min.js',
//   import.meta.url,
// ).toString();

pdfjs.GlobalWorkerOptions.workerSrc = `https://unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.js`;

export default function PdfViewer({ pdfUrl }) {
  
  return (
    <div>
      <Document
        file={pdfUrl}
        onLoadSuccess={({ numPages }) => console.log(`Document loaded with ${numPages} pages.`)}
        onLoadError={(error) => console.error('Error occurred while loading document:', error.message)}
      >
        <Page pageNumber={1} />
      </Document>
    </div>

  );
};
