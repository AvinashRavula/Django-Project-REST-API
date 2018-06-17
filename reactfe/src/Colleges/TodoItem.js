import React, { Component } from 'react'


class TodoItem extends Component{
    render(){
        return (
                <li className="checked">{this.props.text}</li>
        )
    }
}

export default TodoItem