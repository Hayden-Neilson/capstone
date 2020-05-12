import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
// import axios from "axios";
import Home from "./home";
import NavigationContainer from "../components/navigation-container/navigation";
import About from "./about";

export default class App extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div className="container">
        <Router>
          <div>
            <NavigationContainer />

            <Switch>
              <Route exact path="/" component={Home} />
              <Route path="/About" component={About} />
            </Switch>
          </div>
        </Router>
      </div>
    );
  }
}

// import React, { useContext, useEffect } from 'react';

// function App  {
//   useEffect(() => {
//     fetch('/')
//   })
//     return (
//       <div className='app'>
//         <h1>Scraper to find a job</h1>
//       </div>
//     );
