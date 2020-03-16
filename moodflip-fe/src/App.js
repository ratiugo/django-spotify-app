import React, {Component} from "react";
import axios from "axios";
import "./App.css";

import {API_URL} from "./constants";

import LoadingScreen from "./components/loadingScreen/LoadingScreen";

class App extends Component {

  constructor(){
    super();
    this.state = {
      loggedIn: "false",
      loading: "false"
    }
  }

  setLoadingScreen = () => {
    this.setState({
      loggedIn: "false",
      loading: "true"
    });
  }

  getUserPlaylistsTracks = () => {
    axios.get(API_URL+"login")
      .then(() => this.setState({loggedIn: "true", loading: "false"}));
  }

  login = () => {
    this.setLoadingScreen();
    this.getUserPlaylistsTracks();
  }

  loggingIn = () => {
    switch(this.state.loading){
      case("false"):
        switch(this.state.loggedIn){
          case("false"):
            return(
              <button onClick = {this.login}>
               loginogin
              </button>
            );
          case("true"):
            return(
                <div>
                  woo it worked
                </div>
              );
          default:
            return(
              <button onClick = {this.login}>
               loginogin
              </button>
            );
        }

      case("true"):
        return(
          <LoadingScreen />
        );

      default:
        return(
          <button onClick = {this.login}>
           loginflop
          </button>
        );
    }
  }

  render(){
    return(
      <div>
        {this.loggingIn()}
      </div>
    );
  }
}

export default App;

