import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Pagination extends Component {
  constructor(props) {
    super(props);

    this.state = {
      activeIndex: 1,
      pagination: [1, 2, 3, 4]
    };
  }

  createPaginationArray(start, limit) {
    const arr = [];

    for (let i = 0; i < limit; i++) {
      arr.push(start + i);
    }

    return arr;
  }

  updatePagination(page) {
    this.setState({ activeIndex: page });

    const { pagination } = this.state;

    if (
      pagination.indexOf(page) == -1 &&
      page > pagination[pagination.length - 1]
    ) {
      const updatedPagination = this.createPaginationArray(page, 4);
      this.setState({ pagination: updatedPagination });
    } else if (
      pagination.indexOf(page) == -1 &&
      page < pagination[0] &&
      page > 0
    ) {
      const updatedPagination = this.createPaginationArray(page - 3, 4);
      this.setState({ pagination: updatedPagination });
    }
  }

  incrementPagination() {
    const { activeIndex } = this.state;
    const { maxPages } = this.props;

    if (activeIndex + 1 <= maxPages) {
      const updatedIndex = activeIndex + 1;
      this.setState({ activeIndex: updatedIndex });

      this.handleClick(updatedIndex);
    }
  }

  decrementPagination() {
    const { activeIndex } = this.state;

    if (activeIndex - 1 >= 1) {
      const updatedIndex = activeIndex - 1;
      this.setState({ activeIndex: updatedIndex });

      this.handleClick(updatedIndex);
    }
  }

  handleClick(page) {
    const { handleSearch } = this.props;

    handleSearch(page);
    this.updatePagination(page);

    // scroll to top
    window.scrollTo(0, 0);
  }

  renderPagination() {
    const { pagination, activeIndex } = this.state;

    return pagination.map((page, i) => {
      return (
        <span
          className={`${page == activeIndex ? 'active' : undefined}`}
          key={i}
          onClick={() => this.handleClick(page)}
        >
          {page}
        </span>
      );
    });
  }

  render() {
    return (
      <div className="pagination__container">
        <div className="pagination">
          <span onClick={() => this.decrementPagination()}>&laquo;</span>

          {this.renderPagination()}

          <span onClick={() => this.incrementPagination()}>&raquo;</span>
        </div>
      </div>
    );
  }
}

Pagination.propTypes = {
  maxPages: PropTypes.number.isRequired,
  handleSearch: PropTypes.func.isRequired
};

export default Pagination;
