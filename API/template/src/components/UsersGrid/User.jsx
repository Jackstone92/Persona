import React from 'react';
import PropTypes from 'prop-types';

import GoogleMapReact from 'google-map-react';



const User = props => {
  const { image, username, name, current_location } = props;

  const lat = current_location[0];
  const lon = current_location[1];

  return (
    <div className="card">
      <div className="card__image-container">
        <img className="card__image" src={image} alt="" />
      </div>

      <svg className="card__svg" viewBox="0 0 800 500">
        <path
          d="M 0 100 Q 50 200 100 250 Q 250 400 350 300 C 400 250 550 150 650 300 Q 750 450 800 400 L 800 500 L 0 500"
          stroke="transparent"
          fill="#333"
        />
        <path
          className="card__line"
          d="M 0 100 Q 50 200 100 250 Q 250 400 350 300 C 400 250 550 150 650 300 Q 750 450 800 400"
          stroke="pink"
          strokeWidth="3"
          fill="transparent"
        />
      </svg>

      <div className="card__content">
        <h1 className="card__title">{username}</h1>
        <h2>{name}</h2>
        <hr />
        <p />
      </div>
    </div>
  );
};

User.propTypes = {
  image: PropTypes.string,
  username: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  current_location: PropTypes.array.isRequired
};

/*address: "09 Knight parkways↵West Yvonneshire↵HD23 5NJ"
birthdate: "1989-07-07"
blood_group: "AB+"
company: "Smith, Haynes and Hooper"
current_location: Array(2)
0: -66.491849
1: -69.512524
job: "Solicitor"
mail: "jshort@hotmail.com"
name: "Dr. Mohamed Newton"
residence: "1 Bruce alley↵New Justin↵L07 2TE"
sex: "F"
ssn: "ZZ376803T"
username: "mauriceharris"
website: Array(4)
0: "https://www.holmes-saunders.com/"
1: "http://foster-ford.com/"
2: "https://www.farrell-evans.com/"
3: "http://white-kelly.net/"
*/

export default User;
