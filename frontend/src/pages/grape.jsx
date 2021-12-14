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
                    src="https://www.thespruce.com/thmb/Suw__ewHkDRx5gGtaNj_5FCKuyE=/2370x1580/filters:fill(auto,1)/thespruce.com-how-to-grow-grapes-4774749-8-ef6c54d6aea14d7b9b964006ff10c850.jpg"
                    width="300px"
                    height="200px"
                />

                <h2 style={{color: '#015249'}}> Grape </h2>
                    <a href="https://en.wikipedia.org/wiki/Grape"> Grape - Wikipedia </a> 
                <p>
                    A grape is a fruit, botanically a berry, of the deciduous woody vines of the flowering plant genus Vitis.
                    Grapes can be eaten fresh as table grapes, used for making wine, jam, grape juice, jelly, grape seed extract, vinegar, 
                    and grape seed oil, or dried as raisins, currants and sultanas
                </p>

                <h2 style={{color: '#015249'}}> Companion crops </h2>
                <p> 
                    <a href="https://www.gardeningknowhow.com/edible/fruits/grapes/grape-companion-planting.htm"> 
                            Grape Companion Plants from Gardening Know How </a> </p>
                <p>        
                    Excellent companions for grapes include: 
                    <ul>
                        <li> Hyssop </li>
                        <li> Oregano </li>
                        <li> Basil </li>
                        <li> Beans </li>
                        <li> Blackberries </li>
                        <li> Clover </li>
                        <li> Geraniums </li>
                        <li> Peas </li>
                    </ul>
                </p>

                <h2 style={{color: '#015249'}}> Common crop diseases and prevention </h2>

                <h3> Grape Black Rot - Botryosphaeria obtusa </h3>

                <a href="https://en.wikipedia.org/wiki/Botryosphaeria_obtusa"> 
                        Botryosphaeria obtusa - Wikipedia </a> 
                <p>        
                    Botryosphaeria obtusa is a plant pathogen that causes frogeye leaf spot, black rot and cankers on many plant species.[1] On the leaf it is referred 
                    to as frogeye leaf spot; this phase typically affects tree and shrubs. In fruit such as the apple, cranberry and quince, it is referred to as black rot, 
                    and in twigs and trunks it causes cankers.[1]
                </p>
                
                <h3> Treatment and Prevention </h3> 
        
                <p>
                    The most effective treatment is to prune out the infected areas on trees, to ensure transfer between trees does not occur. Fruit that is infected can stay 
                    on the tree for over a year, and therefore remaining fruit should be removed to avoid another source of inoculation for other trees. The trimmed branches or dead 
                    fruit should then be burned or disposed of immediately as the organism can survive on the dead tissue for a long period of time. Infection of leaves and fruit can be 
                    avoided by spraying them with a fungicide. The treatment for the fungicide should be also kept up to date via the manufacturer's instructions.[2]
                </p>

                <h3> Grape Esca (Black Measles) </h3>
                <a href="https://en.wikipedia.org/wiki/Esca_(grape_disease)"> Esca (grape disease) - Wikipedia </a>
                <img 
                    src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/ESCA_Blattsymptom_1.JPG/330px-ESCA_Blattsymptom_1.JPG"
                    width="300px"
                    height="200px"
                />
                <p> 
                    Esca is a grape disease of mature grapevines. It is a type of grapevine trunk disease. The fungi Phaeoacremonium aleophilum, Phaeomoniella chlamydospora[1] and Fomitiporia mediterranea[2]
                    are associated with the disease. 
                </p>

                <h3> Treatment and Prevention </h3>
                <p> Protection from initial inoculation, either via sexual ascospores or asexual conidia, with fungicide is the main form of pathogen management. Spray schedules should 
                    be created with plant and pathogen development timings in mind and thus should begin with an initial spray at budswell and repeated in 10 to14 day intervals.
                </p>
            </div>
        </Container>
    </div>
  );
}
export default CropProfile;