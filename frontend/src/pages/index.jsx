import React from "react";
import {Link} from "react-router-dom";
import logo from '../logo.svg';
import '../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {
  Container,
  Card,
  Row,
  Button
} from 'react-bootstrap';
import MainNavbar from '../components/mainNavbar';
import CropCarouselWidget from "../components/cropCarouselWidget";

const Home = () => {
      return (
        <div className="App">    
          <MainNavbar></MainNavbar>
    
          <Container>
            <Row className="justify-content-md-center">
              <Card style={{width: '20rem', borderColor: '#57BC90', borderWidth: '5px', margin: "10px"}}>
                <Card.Body>
                  <Card.Title>Weather</Card.Title>
                  <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
                  <Card.Text>
                    Some quick example text to build on the card title and make up the bulk of
                    the card's content.
                  </Card.Text>
                  <Card.Link href="#">Card Link</Card.Link>
                  <Card.Link href="#">Another Link</Card.Link>
                </Card.Body>
              </Card>
    
              <Card style={{width: '20rem', borderColor: '#57BC90', borderWidth: '5px', margin: "10px"}}>
                <Card.Body>
                    <Card.Title>
                      <div style={{fontSize: '100px', color: '#57BC90'}}>13</div>
                    </Card.Title>
                    <Card.Subtitle className="mb-2 text-muted">crops have been infected</Card.Subtitle>
                </Card.Body>
              </Card>
            </Row>
    
            <br></br>
    
            <Row className="justify-content-md-center">
              <Card style={{width: '25rem', borderColor: '#57BC90', borderWidth: '5px', margin: "10px"}}>
                <Card.Body>
                  <Card.Title>My Crop</Card.Title>
                  <CropCarouselWidget></CropCarouselWidget>
                </Card.Body>
              </Card>
              
              <Card style={{borderWidth: '0px', width: '15rem', margin: "10px"}}>
                <Card.Body>
                    <div className='mb-3'>
                        <Button variant="success" size="lg">
                            Upload crop photo
                        </Button>  
                    </div>

                    <div>
                        <Button variant="success" size="lg">
                            Profile Settings
                        </Button>  
                    </div>       
                </Card.Body>
              </Card>
            </Row>
          </Container>
        </div>
      );
    }

export default Home;