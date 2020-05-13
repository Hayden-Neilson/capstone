import React from "react";
// import axios from "axios";
import { withRouter } from "react-router";
import { NavLink } from "react-router-dom";

export default function footer() {
  return (
    <div className="footer">
      <div className="footer-link-wrapper">
        <NavLink exact to="/" activeClassName="nav-link-active">
          Home
        </NavLink>
      </div>

      <div className="nav-link-wrapper">
        <NavLink to="/about" activeClassName="nav-link-active">
          About
        </NavLink>
      </div>

      <div className="copyright">
        &copy; 2020 Scraper for your new job &#124; All rights reserved ( This
        is for my Bottega Project )
      </div>
    </div>
  );
}
