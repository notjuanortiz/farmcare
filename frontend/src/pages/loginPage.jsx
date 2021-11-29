import React, { useState } from "react";
import MainNavbar from '../components/mainNavbar';
import {
  Container,
  Button,
  Form
} from 'react-bootstrap';
import { authenticationService } from "../services/authentication.service";

const LoginPage = () => {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();

  return (
    <div>
        <MainNavbar></MainNavbar>
    
        <Container style={{width: '500px'}}>
            <Form onSubmit= {(e) => {
              e.preventDefault()
              authenticationService.login(email,password);
            }}>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control type="email" placeholder="Enter email" onChange={(e) => setEmail(e.target.value)}/>
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)}/>
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