import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import PropTypes from 'prop-types';

const Navbar = withRouter(({ history, isActive, handleCloseNavigation }) => (
  <div className={`nav`}>
    <div className="nav__content">
      <ul className="nav__list">
        <li
          className="nav__list-item"
          onClick={() => {
            handleCloseNavigation();
            history.push('/');
          }}
        >
          Find Persona
        </li>
        <li
          className="nav__list-item"
          onClick={() => {
            handleCloseNavigation();
            history.push('/all-personas');
          }}
        >
          All Persona
        </li>
      </ul>
    </div>
  </div>
));

Navbar.propTypes = {
  isActive: PropTypes.bool.isRequired,
  handleCloseNavigation: PropTypes.func.isRequired
};

export default Navbar;
