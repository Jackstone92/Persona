import React, { Component } from 'react';
import PropTypes from 'prop-types';

class SearchBar extends Component {
  handleKeyDown(e) {
    if (e.key === 'Enter') {
      this.props.onSearchEnterKey();
    }
  }

  render() {
    const { value, onSearchChange } = this.props;

    return (
      <div className="search__container">
        <input
          className="search__input"
          type="text"
          placeholder="Search Personas By Username"
          autoComplete="off" 
          autoCorrect="off" 
          autoCapitalize="off" 
          spellCheck="false" 
          value={value}
          onChange={e => onSearchChange(e)}
          onKeyPress={e => this.handleKeyDown(e)}
        />
      </div>
    );
  }
}

SearchBar.propTypes = {
  value: PropTypes.string.isRequired,
  onSearchChange: PropTypes.func.isRequired,
  onSearchEnterKey: PropTypes.func.isRequired
};

export default SearchBar;
