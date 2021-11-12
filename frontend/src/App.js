import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {
  Navbar,
  Container,
  Offcanvas,
  NavDropdown,
  Form,
  Button,
  FormControl,
  Nav,
  Card,
  Row
} from 'react-bootstrap';
import MainNavbar from './components/mainNavbar';

function App() {
  return (
    <div className="App">    
      <MainNavbar></MainNavbar>

      <div>
        <Row>
          <Card style={{width: '18rem', borderColor: '#57BC90', borderWidth: '5px', marginRight: "10px"}}>
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

          <Card style={{width: '18rem', borderColor: '#57BC90', borderWidth: '5px'}}>
            <Card.Body>
              <Card.Title>Crops infected</Card.Title>
              <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
              <Card.Text>
                Some quick example text to build on the card title and make up the bulk of
                the card's content.
              </Card.Text>
              <Card.Link href="#">Card Link</Card.Link>
              <Card.Link href="#">Another Link</Card.Link>
            </Card.Body>
          </Card>
        </Row>

        <br></br>

        <Row>
          <Card style={{width: '18rem', borderColor: '#57BC90', borderWidth: '5px', marginRight: "10px"}}>
            <Card.Body>
              <Card.Title>My Crop</Card.Title>
              <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
              <Card.Text>
                Some quick example text to build on the card title and make up the bulk of
                the card's content.
              </Card.Text>
              <Card.Link href="#">Card Link</Card.Link>
              <Card.Link href="#">Another Link</Card.Link>
            </Card.Body>
          </Card>
          
          <Card style={{width: '18rem', borderColor: '#57BC90', borderWidth: '5px'}}>
            <Card.Body>
              <Card.Title>Buttons</Card.Title>
              <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
              <Card.Text>
                Some quick example text to build on the card title and make up the bulk of
                the card's content.
              </Card.Text>
              <Card.Link href="#">Card Link</Card.Link>
              <Card.Link href="#">Another Link</Card.Link>
            </Card.Body>
          </Card>
        </Row>
      </div>
    </div>
  );
}

export default App;
