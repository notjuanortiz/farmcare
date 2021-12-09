import React from "react";
import {Link,  useHistory} from "react-router-dom";
import '../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {
  Container,
  Card,
  Row,
  Button,
  Table
} from 'react-bootstrap';
import MainNavbar from '../components/mainNavbar';

const LandingPage = () => { 

      return (
        <div className="App">    
          <MainNavbar></MainNavbar>
    
          <Container>
           <h1 className="mb-4">Manage, Discover, Grow</h1>
           <div style={{width: "50%", margin: "auto"}}>
              Our goal at FarmCare is to provide an all-in-one application that makes farming 
              more efficient, improves yield, and delivers increased profit. Our approach is 
              different as we are helping local farmers get started by using Machine Learning 
              and Computer Vision. With these technologies, FarmCare is there to educate 
              farmers about their crop and help increase annual yield by providing key insights
               that can be leveraged quickly and efficiently. These insights are delivered to 
               the farmers via timely smart alerts that allow them to make better real time 
               decisions and maximize profit. And it’s all done through a simple, beautiful,
                and easy-to-use interface. 
           </div>

           <Link to="/sign-up" className="btn btn-lg btn-success mt-3 mb-5 m-1">Sign up</Link>
           <Link to="/login" className="btn btn-lg btn-success mt-3 mb-5 m-1">Login</Link>

           <Table borderless style={{width: "50%", margin: "auto"}} className="mt-5">
              <tbody>
                <tr>
                  <td>
                    <div className="text-muted">Farm more acres of land</div>
                  </td>
                  <td>
                    <div className="text-muted">Spend less time learning</div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div className="text-muted">Improve yields and profitability</div>
                  </td>
                  <td>
                    <div className="text-muted">Make wiser decisions and stay ahead of competition</div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div className="text-muted">Identify upcoming weather problems before they affect yield</div>
                  </td>
                  <td>
                    <div className="text-muted">Save time and gain peace of mind</div>
                  </td>
                </tr>  
              </tbody>
            </Table>
          </Container>
        </div>
      );
    }

export default LandingPage;