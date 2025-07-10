// src/components/Navbar.jsx
import React from 'react';

const Navbar = () => {
  return (
    <nav style={styles.nav}>
      <div style={styles.logo}>🧠 CT Analysis Report</div>
      <div>
        <a href="#" style={styles.link}>Home</a>
        <button style={styles.button}>Upload</button>
      </div>
    </nav>
  );
};

const styles = {
  nav: {
    display: 'flex',
    justifyContent: 'space-between',
    padding: '1rem 2rem',
    borderBottom: '1px solid #ddd',
    alignItems: 'center',
  },
  logo: {
    fontWeight: 'bold',
  },
  link: {
    marginRight: '1rem',
    textDecoration: 'none',
    color: '#333'
  },
  button: {
    backgroundColor: '#000',
    color: '#fff',
    border: 'none',
    padding: '6px 12px',
    borderRadius: '6px',
    cursor: 'pointer'
  }
};

export default Navbar;
