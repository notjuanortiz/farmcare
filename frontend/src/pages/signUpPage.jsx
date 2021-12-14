import React from "react";
import MainNavbar from '../components/mainNavbar';
import {
  Container,
  Button,
  Form,
  InputGroup
} from 'react-bootstrap';
import ReCAPTCHA from 'react-google-recaptcha';
import { useState } from "react";

const SignUpPage = () => {

  const [submit, setSubmit] = useState(false);
  const [userEmail, setUserEmail] = useState("");
  const [pass1, setPass1] = useState("");
  const [pass2, setPass2] = useState("");
  const [match, setMatch] = useState(false);

  function onChange(value) {
    setSubmit(true);
  }

  const onChangeEmail = (e) => {
    const myEmail = e.target.value;
    setUserEmail(myEmail);
  };

  const onChangePassword1 = (e) => {
    const pass_1 = e.target.value;
    setPass1(pass_1);
  };

  const onChangePassword2 = (e) => {
    const pass_2 = e.target.value;
    setPass2(pass_2);
  };

  function createNewUser(){
    if(pass1 != pass2) {
      setMatch(true);
    }
    else {
      const auth_token = localStorage.getItem("access-token");
      fetch('http://localhost:8000/auth/registration/', {
        method: 'POST',
        headers: {
          'Content-Type' : 'image/jpeg',
          'Authorization': `Bearer ${auth_token}`
        },
        body: {
          email: userEmail,
          password1: pass1,
          password2: pass2
        }
      })
      .catch(err=>{
        console.log("new user not created: ",err)
      })
    }
  }

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
                    <Form.Control type="email" placeholder="Enter email" onChange={onChangeEmail} />
                    {/* <Form.Text className="text-muted">
                        We'll never share your email with anyone else.
                    </Form.Text> */}
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicPassword1">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Enter Password" onChange={onChangePassword1} />
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicPassword2">
                    <Form.Label>Confirm password</Form.Label>
                    <Form.Control type="password" placeholder="Confirm Password" onChange={onChangePassword2} />
                </Form.Group>

                { match ? <div className="text-danger">Passwords do not match.</div> : <></> }
                
                <div className="App">
                  <ReCAPTCHA
                    sitekey="6LeYyoMdAAAAAGF90MQe9mj_oAIZcdWNFP8_opwv"
                    onChange={onChange}
                  />
                </div>

                <div>
                  { submit ? 
                    <Button className="mt-2" variant="success" type="submit"
                      onClick={() => {
                        createNewUser()
                      }}
                    >
                      Submit
                    </Button> 
                    : <></> }
                </div>
            </Form>
        </Container>
    </div>
  );
}
export default SignUpPage;