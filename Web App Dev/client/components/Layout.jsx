import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Layout.css';

export default function Layout({ children }) {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <div>
      <header className="navbar">

<div className="logo">
  <Link to="/">
    <img src="src/assets/logo.png" alt="ICR Logo" className="logo-img"/>
  </Link>
</div>



        <nav className={`nav-links ${menuOpen ? 'open' : ''}`}>
          <Link to="/" onClick={() => setMenuOpen(false)}>Home</Link>
          <Link to="/about" onClick={() => setMenuOpen(false)}>About</Link>
          <Link to="/project" onClick={() => setMenuOpen(false)}>Projects</Link>
          <Link to="/education" onClick={() => setMenuOpen(false)}>Education</Link>
          <Link to="/services" onClick={() => setMenuOpen(false)}>Services</Link>
          <Link to="/contact" onClick={() => setMenuOpen(false)}>Contact</Link>
        </nav>

        <div className="hamburger" onClick={() => setMenuOpen(!menuOpen)}>
          <div></div>
          <div></div>
          <div></div>
        </div>
      </header>

      <main className="content">{children}</main>
    </div>
  );
}
