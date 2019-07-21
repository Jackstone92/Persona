import React from 'react';
import PropTypes from 'prop-types';

const Hamburger = props => {
  return (
    <div
      className="menu-icon"
      onClick={props.handleHamburgerClicked.bind(this)}
    >
      <span className="menu-icon__line menu-icon__line-left" />
      <span className="menu-icon__line" />
      <span className="menu-icon__line menu-icon__line-right" />
    </div>
  );
};

Hamburger.propTypes = {
  handleHamburgerClicked: PropTypes.func.isRequired
};

export default Hamburger;
