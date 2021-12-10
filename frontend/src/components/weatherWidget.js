import 'bootstrap/dist/css/bootstrap.min.css';
import {
  Card,
  Table
} from 'react-bootstrap';
import { useState, useEffect } from "react";

const WeatherWidget = () => {

  const [temp, setTemp] = useState("");
  const [desc, setDesc] = useState("");
  const [icon, setIcon] = useState("");
  const [humidity, setHumidity] = useState("");
  const [wind, setWind] = useState("");
  const [pressure, setPressure] = useState("");

  useEffect(() => {
    const apiKey = "6e27a113797392f6dee5a23a3d7cc5ef";
    const zipcode = "11783";

    fetch(`http://api.openweathermap.org/data/2.5/weather?zip=${zipcode},us&appid=${apiKey}`)
      .then(res => res.json())
      .then(result => { 
          let description = result.weather[0].description;
          console.log("desc",description);
          setDesc(description);

          let path = `weather_icons/${result.weather[0].icon}.png`;
          setIcon(path);

          setHumidity(result.main.humidity);

          setWind(result.wind.speed);

          setPressure(result.main.pressure);

          let temperature = result.main.temp;
          temperature = (temperature - 273.15) * (9/5) + 32; 
          temperature = Math.trunc(temperature);         
          setTemp(temperature);
      });
  });

  if(temp < 40) {
    const auth_token = localStorage.getItem("access");
    fetch('http://localhost:8000/alerts', {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        authorization: auth_token
      },
      body: {
        body: `Alert! The temperature dropped to 40 degree farenheit.
         Please keep in mind that this temperature is hazardous for most plants.`,
        to: "ananaziz98@gmail.com"
      }
    })
  }

  return (
    <div>
        <Card.Body>
          <p>
            <img style={{width: '50px', height: '50px'}} src={icon} alt="logo" />
          </p>
          <p>
            <Card.Subtitle className="mb-2 text-muted">{desc}</Card.Subtitle>
          </p>
          <Card.Title>
            <Table bordered>
              <tbody>
                <tr>
                  <td>
                    {temp}<span>&#176;</span> F <br/>
                    <span style={{fontSize: '12px'}} className="text-muted">Temperature</span>
                  </td>
                  <td>
                    {humidity} % <br/>
                    <span style={{fontSize: '12px'}} className="text-muted">Humidity</span>
                  </td>
                </tr>
                <tr>
                  <td>
                    {wind} km/h <br/>
                    <span style={{fontSize: '12px'}} className="text-muted">Wind Speed</span>
                  </td>
                  <td>
                    {pressure} mb<br/>
                    <span style={{fontSize: '12px'}} className="text-muted">Pressure</span>
                  </td>
                </tr> 
              </tbody>
            </Table>
          </Card.Title>
        </Card.Body>
    </div>
  );
}

export default WeatherWidget;