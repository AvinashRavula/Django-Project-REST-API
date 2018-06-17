import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
// import ExampleComponent from './ExampleComponent';
// import PropsExample from './PropsExample'
// import StateExample from './StateExample'
import CollegeListContainer from './Colleges/CollegeContainer'   
import StudentListContainer from './Students/StudentListContainer'
import {Header,Heading} from './Header'
import {
  BrowserRouter as Router,
  Route,
  Link,
  Redirect,
  withRouter,
  Switch
} from "react-router-dom";
import Cookies from 'universal-cookie';
import Login from './Authentication/Login'

class App extends Component {
  state = {
    title : "All Participating Colleges",
    isAuthenticated : false,
    username:''
  }
  cookies = new Cookies();

  constructor(){
    super();
    if (this.cookies.get('userJwtToken') != '')
    {
      this.updateLoginStatus(true);
    }
  }
  
  updateTitle = (title) => {
    this.setState({title});
  }
  
  updateLoginStatus = (isAuthenticated) => {
    this.setState({isAuthenticated})
  }

  updateUsername = (username) => {
    this.setState({username})
  }


  render() {
    return (
      <div>
        <Header title="Mentor App" isAuthenticated={this.state.isAuthenticated}
         username={this.state.username} updateUsername={this.updateUsername} 
         updateStatus={this.updateLoginStatus}/>
        <Heading title={this.state.title}/>
        <Router>
          <Switch>
          {/* <Router.Fragment> */}
          
              <Route exact path="/" render={(props) => this.state.isAuthenticated 
                ? 
                <CollegeListContainer 
                  isAuthenticated={this.state.isAuthenticated}
                  updateHeading={this.updateTitle}
                /> 
                :
                //  <Login 
                //   isAuthenticated={this.state.isAuthenticated}
                //   username={this.state.username} updateUsername={this.updateUsername} 
                //   updateStatus={this.updateLoginStatus}/>
                
                <Redirect to="/login"/>
               }
              />
              <Route exact path="/login" render={(props) =>
                <Login 
                isAuthenticated={this.state.isAuthenticated}
                username={this.state.username} updateUsername={this.updateUsername} 
                updateStatus={this.updateLoginStatus}/>
                }
              />
              <Route exact path="/college/:id" render={(props) =>
                 <StudentListContainer {...props} updateHeading={this.updateTitle} />}/>
                 {/* <Route exact path="/college/:id" component={StudentListContainer}/> */}
          {/* </Router.Fragment> */}
            
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;