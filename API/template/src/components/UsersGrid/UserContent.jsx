import React from 'react';
import PropTypes from 'prop-types';

const UserContent = props => {
  const { email, lat, long, websites } = props;

  return (
    <div className="hover">
      <span>More Details</span>
      <a className="social-link" href={`mailto:${email}`} target="_blank">
        <i className="fa fa-envelope" />
      </a>
      <a
        className="social-link"
        href={`https://www.google.com/maps/search/?api=1&query=${lat},${long}`}
        target="_blank"
      >
        <i className="fa fa-crosshairs" />
      </a>
      {websites.map((url, i) => {
        return (
          <a className="social-link" href={url} target="_blank" key={i}>
            <i className="fa fa-globe" />
          </a>
        );
      })}
    </div>
  );
};

UserContent.propTypes = {
  email: PropTypes.string.isRequired,
  websites: PropTypes.array.isRequired,
  lat: PropTypes.number.isRequired,
  long: PropTypes.number.isRequired,
  websites: PropTypes.array.isRequired
};

export default UserContent;
