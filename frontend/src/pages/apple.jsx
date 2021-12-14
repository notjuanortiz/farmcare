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
                    src="https://www.isons.com/wp-content/uploads/2016/10/apples-on-branch.jpg"
                    width="300px"
                    height="200px"
                />

                <h2 style={{color: '#015249'}}> Apple </h2>
                    <a href="https://en.wikipedia.org/wiki/Apple"> Apple - Wikipedia </a> 
                <p>
                    An apple is an edible fruit produced by an apple tree (Malus domestica)/ Apples grown from seed tend to be very different from those of the parents, 
                    and the resultant fruit frequently lack desired characteristics. There are more than 7,500 known cultivars of apples. Worldwide production of apples 
                    in 2018 was 86 million tonnes, with China accounting for nearly half of the total.
                </p>

                <h2 style={{color: '#015249'}}> Companion crops </h2>
                <p> 
                    <a href="https://www.gardeningknowhow.com/edible/fruits/apples/apple-tree-companions.htm"> 
                            Apple Companion Plants from Gardening Know How </a> </p>
                <p>        
                    There are several different plants that are beneficial apple tree companions. The following plants include apple tree companions that deter pests and enrich 
                    the soil when cut back and left as mulch:
                    <ul>
                        <li> Comfrey </li>
                        <li> Nasturtium </li>
                        <li> Chamomile </li>
                        <li> Coriander </li>
                        <li> Dill </li>
                        <li> Fennel </li>
                        <li> Basil </li>
                        <li> Lemongrass </li>
                        <li> Mint </li>
                        <li> Artemisia </li>
                        <li> Yarrow </li>
                        <li> Daffodil </li>
                        <li> Tansy </li>
                        <li> Marigold </li>
                        <li> Hyssop </li>
                    </ul>
                </p>

                <h2 style={{color: '#015249'}}> Common crop diseases and prevention </h2>

                <h3> Apple Black Rot - Botryosphaeria obtusa </h3>
                <img 
                    src="https://gardenerspath.com/wp-content/uploads/2019/08/Frogeye-spots-Botryosphaeria-obtusa-on-apple-leaf-FB.jpg"
                    width="300px"
                    height="200px"
                />
                <a href="https://www.gardeningknowhow.com/edible/fruits/apples/apple-tree-companions.htm"> 
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

                <h3> Apple Apple Scab </h3>
                <a href="https://en.wikipedia.org/wiki/Venturia_inaequalis"> Venturia inaequalis - Wikipedia </a>
                <img 
                    src="https://ag.umass.edu/sites/ag.umass.edu/files/fact-sheets/images/apple-scab_02a.jpg"
                    width="300px"
                    height="200px"
                />
                <p> Venturia inaequalis is an ascomycete fungus that causes the apple scab disease. </p>

                <h3> Treatment and Prevention </h3>
                <p> Protection from initial inoculation, either via sexual ascospores or asexual conidia, with fungicide is the main form of pathogen management. Spray schedules should 
                    be created with plant and pathogen development timings in mind and thus should begin with an initial spray at budswell and repeated in 10 to14 day intervals.
                </p>

                <h3> Apple - Cedar Apple Rust </h3>
                <a href="https://en.wikipedia.org/wiki/Gymnosporangium_juniperi-virginianae"> Gymnosporangium juniperi-virginianae - Wikipedia </a>
                <img 
                    src="https://upload.wikimedia.org/wikipedia/en/5/54/Cedar-apple_rust_2.jpg"
                    width="300px"
                    height="200px"
                />
                <p> Gymnosporangium juniperi-virginianae is a plant pathogen that causes cedar-apple rust.[1] In virtually any location where apples or crabapples (Malus) and Eastern red-cedar (Juniperus virginiana) 
                    coexist, cedar apple rust can be a destructive or disfiguring disease on both the apples and cedars. Quince and hawthorn are the most common host and many species of juniper can substitute for the 
                    eastern red cedars. 
                </p>

                <h3> Treatment and Prevention </h3>
                <p> Because apples are an economically important crop, control is usually focused there. Interruption of the disease cycle is the only effective method for control of the cedar apple rust. The recommended
                    method of control is to “remove cedars located within a 1 mile (1.6 km) radius” of the apples to interrupt the disease cycle,[4] though this method is seldom practical. For those doing bonsai, it is common 
                    to have the trees within feet of each other and on the central eastern seaboard of the United States, Eastern Red Cedar is a common first-growth conifer along roadsides.
                </p>
            </div>
        </Container>
    </div>
  );
}
export default CropProfile;