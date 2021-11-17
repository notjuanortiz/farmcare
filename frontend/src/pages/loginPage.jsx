import React from "react";
import MainNavbar from '../components/mainNavbar';
import {
  Container,
  Button,
  Form
} from 'react-bootstrap';

const LoginPage = () => {
  return (
    <div>
        <MainNavbar></MainNavbar>
    
        <Container style={{width: '500px'}}>
            <Form>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control type="email" placeholder="Enter email" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" />
                </Form.Group>
                <Button variant="success" type="submit">
                    Submit
                </Button>
            </Form>
        </Container>
    </div>
  );
}
export default LoginPage;