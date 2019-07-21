import React from 'react';
import PropTypes from 'prop-types';

const Header = props => {
  const { title, subtitle } = props;

  return (
    <div className="hero">
      <div className="diagonal-hero-bg">
        <div className="stars">
          <div className="small" />
          <div className="medium" />
          <div className="big" />
        </div>
      </div>
      <div className="hero__title">
        <h1>{title}</h1>
        <h2>{subtitle}</h2>
      </div>
    </div>
  );
};

Header.propTypes = {
  title: PropTypes.string.isRequired,
  subtitle: PropTypes.string.isRequired
};

export default Header;
