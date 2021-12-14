import React from "react";
import MainNavbar from '../components/mainNavbar';
import {
  Container,
  Button,
  Form
} from 'react-bootstrap';
import '../styles/cropProfile.css';
import {Link} from "react-router-dom";

const CropProfile = () => {
  return (
    <div>
        <MainNavbar> </MainNavbar>
    
        <Container style={{width: '700px'}}>
        <Link className="mb-3" to="/home-page">Go back to user dashboard</Link>
            <div class="crop-profile">
                <img 
                    src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Zea_mays_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-283.jpg/330px-Zea_mays_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-283.jpg"
                    width="300px"
                    height="200px"
                />

                <h2 style={{color: '#015249'}}> Corn </h2>
                    <a href="https://en.wikipedia.org/wiki/Maize"> Corn - Wikipedia </a> 
                <p>
                    Maize (/meɪz/ MAYZ; Zea mays subsp. mays, from Spanish: maíz after Taino: mahiz), also known as corn (North American and Australian English), 
                    is a cereal grain first domesticated by indigenous peoples in southern Mexico about 10,000 years ago.
                </p>

                <h2 style={{color: '#015249'}}> Companion crops </h2>
                <p> 
                    <a href="https://www.gardeningknowhow.com/edible/vegetables/corn/corn-companion-planting.htm"> 
                            Corn Companion Plants from Gardening Know How </a> </p>
                <p>        
                    Other companion plants for corn include:
                    <ul>
                        <li> Cucumbers </li>
                        <li> Lettuce </li>
                        <li> Melons </li>
                        <li> Peas </li>
                        <li> Potatoes </li>
                        <li> Sunflowers </li>
                    </ul>
                </p>

                <h2 style={{color: '#015249'}}> Common crop diseases and prevention </h2>

                <h3> Corn (maize) Cercospora leaf spot Gray leaf Spot - Botryosphaeria obtusa </h3>
                <img 
                    src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Gray_leaf_spot_Cercospora_zeae-maydis_5465607.png/330px-Gray_leaf_spot_Cercospora_zeae-maydis_5465607.png"
                    width="300px"
                    height="200px"
                />
                <a href="https://en.wikipedia.org/wiki/Corn_grey_leaf_spot"> 
                        Corn grey leaf spot - Wikipedia </a> 
                <p>        
                    Grey leaf spot (GLS) is a foliar fungal disease that affects maize, also known as corn. GLS is considered one of the most
                    significant yield-limiting diseases of corn worldwide.
                </p>
                
                <h3> Treatment and Prevention </h3> 
        
                <p>
                    In order to best prevent and manage corn grey leaf spot, the overall approach is to reduce the rate of disease growth and expansion. This 
                    is done by limiting the amount of secondary disease cycles and protecting leaf area from damage until after corn grain formation. High risks 
                    for corn grey leaf spot are divided into eight factors, which require specific management strategies.
                </p>

                <h3> Corn (maize) Common Rust </h3>
                <a href="https://en.wikipedia.org/wiki/Puccinia_sorghi"> Puccinia sorghi - Wikipedia </a>
                <img 
                    src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Puccinia_sorghi_Schwein._1538032.jpg/330px-Puccinia_sorghi_Schwein._1538032.jpg"
                    width="300px"
                    height="200px"
                />
                <p>
                    Puccinia sorghi often first appears after silking in maize. The first early symptom includes chlorotic specks on the leaf. The obvious sign of this plant pathogen
                    is golden-brown pustules or bumps on the above-ground surface of the plant tissue. 
                </p>

                <h3> Treatment and Prevention </h3>
                <p> The use of resistant maize hybrids is the best way to manage P. sorghi. There are two types of resistance that exist.[9] The first is partial resistance which results in 
                    fewer rust spots by reducing germination rate. This type of resistance makes P. sorghi less severe by slowing down development of number of urediniospores. The other type of resistance 
                    is qualitative. This type relies on a single gene which provides total resistance to the plant. Other management tactics include foliar application of fungicide and cultural control
                </p>

                <h3> Corn (maize) Northern Leaf Blight </h3>
                <a href="https://en.wikipedia.org/wiki/Northern_corn_leaf_blight">  Northern corn Leaf Blight - Wikipedia </a>
                <img 
                    src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Sporulation_on_leaf.JPG/330px-Sporulation_on_leaf.JPG"
                    width="300px"
                    height="200px"
                />
                <p> Northern corn leaf blight (NCLB) or Turcicum leaf blight (TLB) is a foliar disease of corn (maize) caused by Exserohilum turcicum, the anamorph of the ascomycete Setosphaeria turcica.
                    With its characteristic cigar-shaped lesions, this disease can cause significant yield loss in susceptible corn hybrids.[1]
                </p>

                <h3> Treatment and Prevention </h3>
                <p> Preventative management strategies can reduce economic losses from NCLB. Preventative management is especially important for fields at high risk for disease development. In-season disease 
                    management options, such as fungicides, are also available.
                </p>
            </div>
        </Container>
    </div>
  );
}
export default CropProfile;