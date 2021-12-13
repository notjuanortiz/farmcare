import {
  Button
} from 'react-bootstrap';

const React = require('react')

class Upload extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      file: null
    }
    this.handleChange = this.handleChange.bind(this)
  }
  handleChange(event) {
    this.setState({
      file: URL.createObjectURL(event.target.files[0])
    })
  }

  fileUpload() {
    let randomNum = Math.floor(Math.random()*90000) + 10000;
    const auth_token = localStorage.getItem("access-token");
    fetch('http://localhost:8000/users/add_crop/', {
      method: 'POST',
      headers: {
        'Content-Type' : 'image/jpeg',
        'Authorization': `Bearer ${auth_token}`
      },
      body: {
        name: `image${randomNum}`,
        image: this.file
      }
    })
    .catch(err=>{
      console.log("file not uploaded: ",err)
    })
  }

  render() {
    return (
      <div>
        <input type="file" onChange={this.handleChange}/>
        <img style={{height: "15%", width: "15%"}} src={this.state.file}/>
        {this.state.file ? <Button variant="success" onClick={() => {this.fileUpload()}}>Upload file</Button> : <></>}
      </div>
    );
  }
}
export default Upload;