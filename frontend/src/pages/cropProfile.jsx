import React from "react";
import MainNavbar from '../components/mainNavbar';
import {
  Container,
  Button,
  Form
} from 'react-bootstrap';

const CropProfile = () => {
  return (
    <div>
        <MainNavbar></MainNavbar>
    
        <Container style={{width: '500px'}}>
            <div>
                <img 
                    src="https://www.ocregister.com/wp-content/uploads/2020/07/iStock-1132371208-1.jpg?w=1569"
                    width="300px"
                    height="200px"
                    className="mb-3"
                />

                <h2 style={{color: '#015249'}}>Tomato</h2>

                <p>
                    <em>“A class should have one, and only one reason to change.”</em>
                </p>

                <p>
                    Ideally every class should have one specific purpose and thus they should have very specific names. The name of your class 
                    should be justified by its specific purpose, making the code easy to parse and understand. Refrain from creating a single 
                    large class which serves various purposes and has a generic name.
                </p>

                <h2 style={{color: '#015249'}}>Companion crops</h2>

                <p>        
                    <em>“An entity should be open for extension but closed for modification.”</em>
                </p>

                <p>
                    Write code that are simple and can be built upon. You should be able to add functionality by adding new code instead of changing 
                    existing code. An example could be open source libraries that you download and write code around it to complement it instead of 
                    needing to change the library itself. Your goal is to get to a point where you can never break the core of your system.
                </p>

                <h2 style={{color: '#015249'}}>Common crop diseases and prevention</h2>

                <p>        
                    <em>“An entity should be open for extension but closed for modification.”</em>
                </p>

                <p>
                    Write code that are simple and can be built upon. You should be able to add functionality by adding new code instead of changing 
                    existing code. An example could be open source libraries that you download and write code around it to complement it instead of 
                    needing to change the library itself. Your goal is to get to a point where you can never break the core of your system.
                </p>
            </div>
        </Container>
    </div>
  );
}
export default CropProfile;