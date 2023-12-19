// UPLOAD INTERFACE COMPONENT

import './UploadInterface.css'

import React, {useState,useEffect} from 'react'
import axios from 'axios'

function UploadFile( props ) {
  const [filename, setFilename] = useState('')
  const [files, setFiles] = useState([{}])
  // const [status, setstatus] = useState('')

  let api = 'http://localhost:8000/api'
  const {updateFileList } = props

  const uploadFile = () =>{
    console.log('Save Button clicked!')

    let formData = new FormData();
    formData.append("pdf", filename)

    let axiosConfig = {
      headers: {
        'Content-Type': 'multpart/form-data'
      }
    }
    console.log(formData)

    axios.post(api + '/files/', formData, axiosConfig)
    .then(
      response =>{
        // console.log(response)
        // setstatus('File Uploaded Successfully')
      }
    ).catch(error =>{
      console.log(error)
    })
    .then(updateFileList)
  }

  return (
    <div id="upload-interface">
      <p>Upload a File</p>
      <form >
        <div className="form-group">
          <label htmlFor="exampleFormControlFile1" className="float-left">Browse</label>
          <input type="file" onChange={e => setFilename(e.target.files[0])} className="form-control" />
        </div>
        <button type="button" onClick={uploadFile} className="btn btn-primary float-left mt-2">Upload</button>
        {/* {status ? <h2>{status}</h2>:null} */}
      </form>
    </div>
  )
}

export default UploadFile
