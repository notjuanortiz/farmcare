import 'bootstrap/dist/css/bootstrap.min.css';
import farmcare_logo from '../assets/farmcare_logo.PNG';
import {Link} from "react-router-dom";
import {
  Row,
  Col
} from 'react-bootstrap';
import { useState } from "react";

const CropCarouselWidget = () => {
  const [crop, setCrop] = useState("");
  const [image, setImage] = useState("");
  
  async function getCrop(){
    const auth_token = localStorage.getItem("access-token");
    const response = await fetch('http://localhost:8000/dashboard', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${auth_token}`
      }
    })
    .catch(err=>{
      console.log(err)
    })

    try {
      const json = await response.json();
      const crop = json.user[0].crops[0].name;
      const imageUrl = json.user[0].crops[0].image_url;
      setCrop(crop);
      setImage(imageUrl);

    } catch (error) {
      console.error("err", error);
    }

  }

  getCrop();

    return (
      <>
      <Row>
        <Col>
            <div>
              <Link to="/apple-profile">Apple</Link>
              <img 
                      src="https://www.isons.com/wp-content/uploads/2016/10/apples-on-branch.jpg"
                      width="100px"
                      height="70px"
              />
            </div>
          </Col>
            <Col>
            <div>
              <Link to="/corn-profile">Corn</Link>
              <img 
                      src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Zea_mays_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-283.jpg/330px-Zea_mays_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-283.jpg"
                      width="100px"
                      height="70px"
              />
            </div>
          </Col>
        <Col>
          <div>
            {crop}
            <img scr={image} />
          </div>
        </Col>
      </Row>

      </>
    );
}

export default CropCarouselWidget;