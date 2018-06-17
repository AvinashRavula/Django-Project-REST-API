import React, { Component } from 'react'
import Cookies from 'universal-cookie';
import {Redirect} from 'react-router-dom'
import { withRouter } from 'react-router'

class Login extends Component{
    cookies = new Cookies();
    state = {
        auth_url : 'http://127.0.0.1:8000/api-basictoken-auth/',
        jwt_url : 'http://127.0.0.1:8000/api-jwttoken-auth/',
        buttonName : 'Login',
        username : "" ,
        password: ""
    }

    saveUsername = (event) => {
        const {target : {value}}  = event;
        this.setState({
            username : value
        })
    }

    savePassword = (event) => {
        const {target : {value}} = event;
        this.setState({
            password : value
        })
    }

    submit = (e) => {
        e.preventDefault();
        // const {username, password} = this.state
        this.login(this.state)
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
    login = ({username, password}) =>
    {
        console.log(username + " : "+password);
        var formData  = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        fetch(this.state.jwt_url, { 
            method: 'post',
            body: formData, 
          }) .then(function(response) {
            return response.json();
        })
        .then((myJson) => {
            if ('token' in myJson){
                this.cookies.set('userJwtToken', myJson, { path: '/',expires: new Date(Date.now()+2592000)} );
                this.cookies.set('username',formData.get('username'), {path : '/', expires: new Date(Date.now()+2592000)})
                console.log(this.cookies.get('userJwtToken'));
                this.props.updateUsername(formData.get('username'));
                this.props.updateStatus(true);
                this.setState(prev => ( {buttonName : 'Logout'}));
                this.props.history.push('/');
                console.log("Redirecting....")
            }
            else{
                alert("Invalid Credentials");
            }
        })
        .catch(e => {console.log("Error occured in fetching students..")});
    }

    render(){
        return (
            <div>
                <input onChange={this.saveUsername} type="text" placeholder="Enter username"/><br/>
                <input onChange={this.savePassword} type="password" placeholder="Enter Password"/><br/>
                <button onClick={this.submit} className={"btn btn-primary"} value="Login">Login</button>
            </div>
        )
    }
}

export default withRouter(Login)