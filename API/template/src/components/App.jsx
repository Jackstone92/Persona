import React, { Component } from 'react';
import { Switch, Route, withRouter } from 'react-router-dom';

import Navbar from './Navbar/Navbar';
import Hamburger from './Navbar/Hamburger';
import FindPersonas from './FindPersonas/FindPersonas';
import AllPersonas from './AllPersonas/AllPersonas';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isActiveNavbar: false
    };
  }

  toggleNavigationState() {
    this.setState({ isActiveNavbar: !this.state.isActiveNavbar });
  }

  render() {
    const { isActiveNavbar } = this.state;

    return (
      <div className={`root ${isActiveNavbar ? 'nav-active' : undefined}`}>
        <Hamburger
          handleHamburgerClicked={this.toggleNavigationState.bind(this)}
        />
        <Navbar
          isActive={isActiveNavbar}
          handleCloseNavigation={this.toggleNavigationState.bind(this)}
        />

        <Switch>
          <Route exact path="/" component={FindPersonas} />
          <Route exact path="/all-personas" component={AllPersonas} />
          <Route path="/all-personas/:username" component={AllPersonas} />
        </Switch>
      </div>
    );
  }
}

export default withRouter(App);
