// UPLOAD INTERFACE COMPONENT

import React, {useState,useEffect} from 'react'
import axios from 'axios'

function UploadFile() {
  const [filename, setFilename] = useState('')
  const [files, setFiles] = useState([{}])
  const [status, setstatus] = useState('')

  let api = 'http://localhost:8000/api'

  const saveFile = () =>{
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
        console.log(response)
        setstatus('File Uploaded Successfully')
      }
    ).catch(error =>{
      console.log(error)
    })
  }

  return (
    <div className="container-fluid">
      <p>Upload a File</p>
      <form >
        <div className="form-group">
          <label htmlFor="exampleFormControlFile1" className="float-left">Browse</label>
          <input type="file" onChange={e => setFilename(e.target.files[0])} className="form-control" />
        </div>
        <button type="button" onClick={saveFile} className="btn btn-primary float-left mt-2">Submit</button>
        {status ? <h2>{status}</h2>:null}
      </form>
    </div>
  )
}

export default UploadFile
