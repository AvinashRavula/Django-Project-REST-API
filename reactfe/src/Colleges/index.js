import React, {Component} from 'react'

class TodoHeader extends Component{
    
    render(){
        return (
            <div id="myDIV" className="header">
                <h2 style={{margin:'5px'}}>{this.props.title} </h2>
                <input type="text" id="myInput" placeholder="Title..."/>
                <span onClick="{newElement}" className="addBtn">Add</span>
            </div>
        )
    }
}

export default TodoHeader
