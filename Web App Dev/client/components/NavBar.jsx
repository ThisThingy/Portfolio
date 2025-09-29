import React from "react";
import { Link } from "react-router-dom";
import logo from "./assets/react.svg"; // replace with your custom logo later

export default function Navbar() {
  return (
    <nav style={{ padding: "1rem", backgroundColor: "#282c34", display: "flex", alignItems: "center" }}>
      <img src={logo} alt="Logo" style={{ width: "40px", marginRight: "1rem" }} />
      <Link to="/" style={{ color: "white", margin: "0 1rem" }}>Home</Link>
      <Link to="/about" style={{ color: "white", margin: "0 1rem" }}>About</Link>
      <Link to="/projects" style={{ color: "white", margin: "0 1rem" }}>Projects</Link>
      <Link to="/education" style={{ color: "white", margin: "0 1rem" }}>Education</Link>
      <Link to="/services" style={{ color: "white", margin: "0 1rem" }}>Services</Link>
      <Link to="/contact" style={{ color: "white", margin: "0 1rem" }}>Contact</Link>
    </nav>
  );
}
