import 'bootstrap/dist/css/bootstrap.min.css';
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
        <Navbar bg="light" expand={false}>
          <Container fluid>
            <Navbar.Brand href="#">farmCare</Navbar.Brand>
            <Navbar.Toggle aria-controls="offcanvasNavbar" />
            <Navbar.Offcanvas
              id="offcanvasNavbar"
              aria-labelledby="offcanvasNavbarLabel"
              placement="end"
            >
              <Offcanvas.Header closeButton>
                <Offcanvas.Title id="offcanvasNavbarLabel">Offcanvas</Offcanvas.Title>
              </Offcanvas.Header>
              <Offcanvas.Body>
                <Nav className="justify-content-end flex-grow-1 pe-3">
                  <Nav.Link href="#action1">Home</Nav.Link>
                  <Nav.Link href="#action2">About</Nav.Link>
                  <Nav.Link href="#action3">Contact</Nav.Link>
                </Nav>
              </Offcanvas.Body>
            </Navbar.Offcanvas>
          </Container>
        </Navbar>
        </div>
  );
}

export default MainNavbar;