import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Switch
} from "react-router-dom";
import LandingPage from "./pages"
import HomePage from "./pages/homePage"
import SignUpPage from "./pages/signUpPage"
import LoginPage from "./pages/loginPage"
import CropProfilePage from "./pages/cropProfilePage"

const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" ><LandingPage /></Route>
        <Route exact path="/home-page" ><HomePage /></Route>
        <Route path="/sign-up"><SignUpPage /></Route>
        <Route path="/login"><LoginPage /></Route>
        <Route path="/crop-profile"><CropProfilePage /></Route>
      </Switch>
    </Router>
  );
}

export default App;
