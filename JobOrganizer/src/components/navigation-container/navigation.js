import React from "react";
// import axios from "axios";
import { withRouter } from "react-router";
import { NavLink } from "react-router-dom";

export default function navigation() {
  return (
    <div className="nav-container">
      <div className="left-side">
        <div className="nav-link-wrapper">
          <NavLink exact to="/" activeClassName="nav-link-active">
            Home
          </NavLink>
        </div>

        <div className="nav-link-wrapper">
          <NavLink to="/about" activeClassName="nav-link-active">
            About
          </NavLink>
        </div>
      </div>
    </div>
  );
}
