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
import AppleProfilePage from "./pages/apple"
import GrapeProfilePage from "./pages/grape"
import CornProfilePage from "./pages/corn"

const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" ><LandingPage /></Route>
        <Route exact path="/home-page" ><HomePage /></Route>
        <Route path="/sign-up"><SignUpPage /></Route>
        <Route path="/login"><LoginPage /></Route>
        <Route path="/crop-profile"><CropProfilePage /></Route>
        <Route path="/apple-profile"><AppleProfilePage /></Route>
        <Route path="/grape-profile"><GrapeProfilePage /></Route>
        <Route path="/corn-profile"><CornProfilePage /></Route>
      </Switch>
    </Router>
  );
}

export default App;
