// APP

import './App.css';

import { useState, useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';
import axios from 'axios'

import UploadInterface from './components/UploadInterface/UploadInterface.jsx';
import FileList from './components/FileList/FileList.jsx';

function App() {
  const [fileList, setFileList] = useState([])

  const updateFileList = async function () {
    try {
      const response = await axios.get(
        "http://localhost:8000/api/files/"
      );
      // console.log(response.data)
      setFileList(response.data);
    } catch (error) {
      console.error('Error fetching data from backend:', error);
      throw error;
    }
  };

  useEffect(() => {
    updateFileList();
  }, []);

  return (
    <div className="App">
      <h1>PDF Search</h1>
      <UploadInterface />
      <FileList fileList={ fileList }/>
    </div>
  );
}

export default App;
