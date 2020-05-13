import React, { Component } from "react";

export default class about extends Component {
  render() {
    return (
      <div className="content-wrapper">
        <div className="title">
          <h1>About </h1>
        </div>

        <div className="center-column">
          <p>
            This website is for new developers, so they can have a easy way to
            look through jobs to apply for these jobs come from the indeed
            website based on certain search criteria!
          </p>
        </div>
      </div>
    );
  }
}
