import './App.css';
import axios from 'axios'

function App() {

  const handleSave = files => {

    const form_data = new FormData();
    for (let i = 0; i < files.length; i++) {
      form_data.append('FILES_' + i, files[i]);
    }
    const url = 'http://localhost:8000/fileuploaderapp/upload/'

    axios({
      url,
      method: 'post',
      data: form_data,
      headers: {
        Accept: 'application/json, text/plain, */*',
      }
    }).then(res => {
        console.log(res.data)
        window.alert('Uploaded Successfully, Page will reload')
        window.location.reload()
      })
      .catch(err => console.log(err))
  }
  return (
    <div className="App">
      <header className="App-header">
        <p>
          <code>File Uploader</code>
        </p>
        <input
          type='file'
          onChange={(e) => handleSave(e.target.files)}
        />
      </header>
    </div>
  );
}

export default App;
