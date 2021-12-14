import 'bootstrap/dist/css/bootstrap.min.css';
import farmcare_logo from '../assets/farmcare_logo.PNG';
import {Link} from "react-router-dom";
import {
  Navbar,
  Container,
  Offcanvas,
  Nav,
  Carousel
} from 'react-bootstrap';
import { useState } from "react";

const CropCarouselWidget = () => {
  const [crop, setCrop] = useState("");
  const auth_token = localStorage.getItem("access-token");
  fetch('http://localhost:8000/dashboard', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${auth_token}`
      }
    })
    .then(response => { 
      console.log("user info: ", response.user);
      let myCrops = response.user.crops;
      setCrop(myCrops);
      console.log("crop profile: ", response)
    })
    .catch(err=>{
      console.log(err)
    })

    return (
      <>
       {crop}
      </>
    );
}

export default CropCarouselWidget;