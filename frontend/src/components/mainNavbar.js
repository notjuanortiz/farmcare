import 'bootstrap/dist/css/bootstrap.min.css';
import farmcare_logo from '../assets/farmcare_logo.PNG';
import {
  Navbar,
  Container,
  Offcanvas,
  NavDropdown,
  Nav,
} from 'react-bootstrap';

function MainNavbar() {
    return (
      <div>
        <Navbar style={{backgroundColor: '#57BC90'}} expand={false}>
          <Container fluid>
            <Navbar.Brand href="#">
              <div style={{display: 'flex'}}>
              <img style={{width: '50px', height: '50px'}} src={farmcare_logo} alt="logo" />
              <h1 style={{color: '#015249'}}>farmCare</h1>
              </div>
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="offcanvasNavbar" />
            <Navbar.Offcanvas
              id="offcanvasNavbar"
              aria-labelledby="offcanvasNavbarLabel"
              placement="end"
            >
              <Offcanvas.Header style={{backgroundColor: "#015249"}} closeButton>
                <Offcanvas.Title id="offcanvasNavbarLabel"></Offcanvas.Title>
              </Offcanvas.Header>
              <Offcanvas.Body style={{backgroundColor: "#015249"}}>
                <Nav className="justify-content-end flex-grow-1 pe-3">
                  <Nav.Link href="#action1"><h4 style={{color: "#ffffff"}}>Home</h4></Nav.Link>
                  <Nav.Link href="#action2"><h4 style={{color: "#ffffff"}}>About</h4></Nav.Link>
                  <Nav.Link href="#action3"><h4 style={{color: "#ffffff"}}>Contact</h4></Nav.Link>
                </Nav>
              </Offcanvas.Body>
            </Navbar.Offcanvas>
          </Container>
        </Navbar>
        <br></br>
        </div>
  );
}

export default MainNavbar;