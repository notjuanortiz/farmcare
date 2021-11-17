import React from "react";
import MainNavbar from '../components/mainNavbar';
import {
  Container,
  Button,
  Form,
  InputGroup
} from 'react-bootstrap';

const SignUpPage = () => {
  return (
    <div>
      <MainNavbar></MainNavbar>
    
      <Container style={{width: '500px'}}>
            <Form>
                <Form.Group className="mb-3" controlId="formBasicFirstName">
                    <Form.Label>First Name</Form.Label>
                    <Form.Control type="text" placeholder="Enter first name" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicLastName">
                    <Form.Label>Last Name</Form.Label>
                    <Form.Control type="text" placeholder="Enter last name" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicPhoneNumber">
                    <Form.Label>Phone Number</Form.Label>
                    <InputGroup>
                      <InputGroup.Text>+1</InputGroup.Text>
                      <Form.Control type="text" placeholder="Enter phone number" />
                    </InputGroup>
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control type="email" placeholder="Enter email" />
                    <Form.Text className="text-muted">
                        We'll never share your email with anyone else.
                    </Form.Text>
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
export default SignUpPage;