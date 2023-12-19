// APP

import './App.css';

import { useState, useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';
import axios from 'axios'

import UploadInterface from './components/UploadInterface/UploadInterface.jsx';

function App() {
  return (
    <div className="App">
      <h1>Upload Files</h1>
      <UploadInterface />
    </div>
  );
}

export default App;
