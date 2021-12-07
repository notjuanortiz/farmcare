import React, { useState } from "react";
import MainNavbar from '../components/mainNavbar';
import {
  Container,
  Button,
  Form
} from 'react-bootstrap';
import { AuthenticationService } from "../services/authentication.service";
import { useHistory } from 'react-router-dom';

const LoginPage = () => {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();
  const history = useHistory();
  const onChangeEmail = (e) => {
    const email = e.target.value;
    setEmail(email);
  };

  const onChangePassword = (e) => {
    const password = e.target.value;
    setPassword(password);
  };

  const authenticate = (e) => {
    e.preventDefault();
    AuthenticationService.login(email, password)
      .then(() => {
        history.push("/");
      });
  };

  return (
    <div>
      <MainNavbar></MainNavbar>

      <Container style={{ width: '500px' }}>
        <Form onSubmit={authenticate}>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Email address</Form.Label>
            <Form.Control type="email" placeholder="Enter email" onChange={onChangeEmail} />
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" placeholder="Password" onChange={onChangePassword} />
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