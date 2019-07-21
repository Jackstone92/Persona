import React from 'react';
import PropTypes from 'prop-types';

import User from './User';
import faker from 'faker';

const UsersGrid = props => {
  const { users, emptyMessage } = props;

  if (users.length > 0) {
    return (
      <div className="users">
        <div className="users__container">
          {users.map((user, i) => {
            const { username, name, current_location } = user;
            
            return (
              <User image={faker.random.image()} username={username} name={name} current_location={current_location} key={i} />
            );
          })}
        </div>
      </div>
    );
  } else {
    return (
      <div className="users">
        <div className="users__container">
          <p>{emptyMessage}</p>
        </div>
      </div>
    );
  }
};

UsersGrid.propTypes = {
  users: PropTypes.array.isRequired,
  emptyMessage: PropTypes.string.isRequired
};

export default UsersGrid;
