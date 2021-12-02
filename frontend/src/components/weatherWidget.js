import 'bootstrap/dist/css/bootstrap.min.css';
import farmcare_logo from '../assets/farmcare_logo.PNG';
import {Link} from "react-router-dom";
import {
  Card
} from 'react-bootstrap';

const WeatherWidget = () => {

  const temperature = [];

    //fetch weather data from openweathermap api needs auth
    async function getWeatherReport() {
      const apiKey = "6e27a113797392f6dee5a23a3d7cc5ef";
      const cityName = "London";
      const response = await fetch(
        `http://api.openweathermap.org/data/2.5/weather?q=${cityName},uk&APPID=${apiKey}`
      );
      const myJson = await response.json();

      const temperature = myJson.weather;

      console.log("today's weather: " , temperature);
    }

    getWeatherReport();

    return (
      <div>
          <Card.Body>
                  <Card.Title>
                    {/* <p>Temperature: 70 C</p>
                    <p>Humidity: 5km/h</p>
                    <p>Wind: 5km/h</p>
                    <p>Precipitation: 0%</p> */}
                    {/* {{temperature}} */}
                  </Card.Title>
                  <Card.Subtitle className="mb-2 text-muted">Good condition for</Card.Subtitle>
                </Card.Body>
      </div>
    );
}

export default WeatherWidget;