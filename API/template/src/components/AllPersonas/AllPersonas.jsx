import React, { Component } from 'react';
import axios from 'axios';
import queryString from 'query-string';

import { ClipLoader } from 'react-spinners';

import Header from '../Header/Header';
import UsersGrid from '../UsersGrid/UsersGrid';
import Pagination from '../UsersGrid/Pagination';

class AllPersonas extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isLoading: false,
      paginationPage:
        this.props.location.search.length > 0
          ? this.checkQueryStringsForPagination()
          : 1,
      users: [],
      totalUsers: 0
    };
  }

  async searchAll(page) {
    this.setState({ isLoading: true });

    try {
      const res = await axios.get(`/people?page=${page}`);
      const data = await res.data;
      const result = await data.result;

      const users = await result.users;
      const totalUsers = await result['total_users'];

      this.setState({ users, totalUsers });
    } catch (error) {
      console.log(error);
    }

    this.setState({ isLoading: false });
  }

  checkQueryStringsForPagination() {
    const qs = this.props.location.search;

    // parse query string
    const values = queryString.parse(qs);
    const page = values.page;

    if (!page) return;

    const paginationPage = parseInt(page);
    return paginationPage;
  }

  changeCurrentPage(numPage) {
    this.setState({ paginationPage: numPage });
    this.searchAll(numPage);
  }

  componentDidMount() {
    this.searchAll(1);
  }

  render() {
    const { users, isLoading, paginationPage, totalUsers } = this.state;

    return (
      <div>
        <Header
          title={'PERSONA'}
          subtitle={'View All The People That Matter'}
        />

        <br />

        {isLoading ? (
          <ClipLoader
            css={{ display: 'block', margin: '0 auto' }}
            sizeUnit={'px'}
            size={500}
            color={'#123abc'}
            loading={true}
          />
        ) : (
          <UsersGrid users={users} emptyMessage={'No Personas were found...'} />
        )}

        <br />

        <Pagination
          handleSearch={this.searchAll.bind(this)}
          maxPages={totalUsers}
        />

        <br />
      </div>
    );
  }
}

export default AllPersonas;
