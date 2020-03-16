import React from "react"

import "./LoadingScreen.css";
import {LOADING_GIF} from "../../images/imageUrls";

const LoadingScreen = () => {
    return(
      <div className = "flex flex-column vh-100 justify-center items-center loading_page_background">
        <p className = "white-90">
            Please wait while ten small slightly spooky yet still soft gremlins grab all of your playlist and track information. They are sometimes slow dudes, and this make take them a few minutes.
        </p>
        <img
            src={LOADING_GIF}
            alt="loading"/>
      </div>
    );
}

export default LoadingScreen;