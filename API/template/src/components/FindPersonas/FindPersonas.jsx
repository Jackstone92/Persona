import React, { Component } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import _ from 'lodash';

import { ClipLoader } from 'react-spinners';

import Header from '../Header/Header';
import SearchBar from '../SearchBar/SearchBar';
import UsersGrid from '../UsersGrid/UsersGrid';


class FindPersonas extends Component {
  constructor(props) {
    super(props);

    this.state = {
      usernameSearchValue: '',
      isLoading: false,
      users: []
    };

    this.debouncedSearch = _.debounce(this.searchByUsername, 300);
  }

  async searchByUsername() {
    this.setState({ isLoading: true });

    const { usernameSearchValue } = this.state;

    if(usernameSearchValue.length > 0) {
      try {
        const res = await axios.get(`/search/${usernameSearchValue}`)
        const data = await res.data;
        const result = await data.result;
        const users = await result.user;
        this.setState({ users})
  
      } catch (error) {
        console.log(error);
      }

    } else {
      this.setState({ users: [] });
    }

    this.setState({ isLoading: false });
  }

  handleSearchQueryTyping(e) {
    e.persist();

    this.setState({ usernameSearchValue: e.target.value });

    if(e.target.value.length > 0) {
      this.debouncedSearch(e);

    } else {
      this.setState({ users: [] });
    }
  }

  handleSearchEnterPress(e) {
    e.persist();

    const { usernameSearchValue } = this.state;

    if(usernameSearchValue.length > 0) {
      this.debouncedSearch(e);

    } else {
      this.setState({ users: [] });
    }
  }

  render() {
    const { users, usernameSearchValue, isLoading } = this.state;

    return (
      <div>
        <Header
          title={'PERSONA'}
          subtitle={'Find The People That Matter'}
        />

        <br />

        <SearchBar
          value={usernameSearchValue}
          onSearchChange={this.handleSearchQueryTyping.bind(this)}
          onSearchEnterKey={this.handleSearchEnterPress.bind(this)}
        />

        <br />

        {
          isLoading ? 
            <ClipLoader
              css={{display: 'block', margin: '0 auto'}}
              sizeUnit={"px"}
              size={500}
              color={'#123abc'}
              loading={true}
            /> 
          : 
            <UsersGrid users={users} emptyMessage={''} /> 
        }        
        <br />
      </div>
    );
  }
}


export default FindPersonas;
