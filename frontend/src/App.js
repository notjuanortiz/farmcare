import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Switch
} from "react-router-dom";
import HomePage from "./pages"
import SignUpPage from "./pages/signUpPage"
import LoginPage from "./pages/loginPage"

const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" ><HomePage /></Route>
        <Route path="/sign-up"><SignUpPage /></Route>
        <Route path="/login"><LoginPage /></Route>
      </Switch>
    </Router>
  );
}

export default App;
