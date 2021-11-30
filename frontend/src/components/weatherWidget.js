import 'bootstrap/dist/css/bootstrap.min.css';
import farmcare_logo from '../assets/farmcare_logo.PNG';
import {Link} from "react-router-dom";
import {
  Card
} from 'react-bootstrap';

const WeatherWidget = () => {
    return (
      <div>
          <Card.Body>
                  <Card.Title>
                    <p>Temperature: 70 C</p>
                    <p>Humidity: 5km/h</p>
                    <p>Wind: 5km/h</p>
                    <p>Precipitation: 0%</p>
                  </Card.Title>
                  <Card.Subtitle className="mb-2 text-muted">Good condition for</Card.Subtitle>
                </Card.Body>
      </div>
    );
}

export default WeatherWidget;