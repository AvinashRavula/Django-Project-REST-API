import React, { Component } from 'react'
import Cookies from 'universal-cookie';
import {Redirect} from 'react-router-dom'


export class Header extends Component{

    cookies = new Cookies();

    state = {
        auth_url : 'http://127.0.0.1:8000/api-basictoken-auth/',
        jwt_url : 'http://127.0.0.1:8000/api-jwttoken-auth/',
        buttonName : 'Login'

    }

    logout = (props) =>
    {
        this.cookies.remove('userJwtToken');
        this.cookies.remove('username');
        console.log(this.cookies.get('userJwtToken'));
        // console.log(formData.get('username'))
        this.props.updateUsername('');
        this.props.updateStatus(false);
        this.setState(prev => ( {buttonName : 'Login'}));
    }
    login = (props) =>
    {
        <Redirect to={{ pathname: '/login', state: { from: this.props.location }}} />
        // var formData  = new FormData();
        // formData.append('username', 'avinash');
        // formData.append('password', 'avinash1229');

        // fetch(this.state.jwt_url, { 
        //     method: 'post',
        //     body: formData, 
        //   }) .then(function(response) {
        //     return response.json();
        // })
        // .then((myJson) => {
        //     // console.log(myJson);
        //     this.cookies.set('userJwtToken', myJson, { path: '/' });
        //     this.cookies.set('username',formData.get('username'), {path : '/'})
        //     console.log(this.cookies.get('userJwtToken'));
        //     // console.log(formData.get('username'))
        //     this.props.updateUsername(formData.get('username'));
        //     this.props.updateStatus(true);
        //     this.setState(prev => ( {buttonName : 'Logout'}));
        // })
        // .catch(e => {console.log("Error occured in fetching students..")});
    }
    
    render(){
        return (
                <div className={"App-header"}>
                    <h1 className={"App-name"}>{this.props.title} </h1>
                    <p className={"App-user"}>
                        <label className={"username"}>
                        { this.props.isAuthenticated ? "Welcome," + this.props.username : "Explore my World by"}</label><br/>
                        <button className={"btn btn-primary login-button"}
                             onClick={
                                    this.props.isAuthenticated?
                                    this.logout : this.login
                                }
                             >
                            { this.props.isAuthenticated? "Logout" : "Login"}
                        </button>
                    </p>
                </div>
        )
    }
}


export const Heading = (props) => {
    return (<h1 className={"center"}>{props.title}</h1>)
}



