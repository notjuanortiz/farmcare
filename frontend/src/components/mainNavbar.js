import 'bootstrap/dist/css/bootstrap.min.css';
import farmcare_logo from '../assets/farmcare_logo.PNG';
import {Link} from "react-router-dom";
import {
  Navbar,
  Container,
  Offcanvas,
  Nav,
} from 'react-bootstrap';

const MainNavbar = () => {
    return (
      <div>
        <Navbar className='mb-5' style={{backgroundColor: '#57BC90'}} expand={false}>
          <Container fluid>
            <Navbar.Brand href="/">
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
                  <Link to="/" ><h5>Home</h5></Link>
                  <Link to="/" ><h5>About</h5></Link>
                  <Link to="/" ><h5>Contact</h5></Link>
                  <Link to="/sign-up" ><h5>Sign Up</h5></Link>
                  <Link to="/login" ><h5>Login</h5></Link>
                </Nav>
              </Offcanvas.Body>
            </Navbar.Offcanvas>
          </Container>
        </Navbar>
        </div>
  );
}

export default MainNavbar;