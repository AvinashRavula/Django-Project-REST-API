import React, { Component } from 'react'
import { Link } from 'react-router-dom' 
import Cookies from 'universal-cookie';

const StudentItem = (props) => {
    return (
        <tr>
            <td><Link to={`/student/${props.student.id}`}>{props.student.name}</Link></td>
            <td>{props.student.email}</td>
            <td>{props.student.dob}</td>
            <td>{props.student.db_folder}</td>
        </tr>
    );
}

const TableHead = (props) => {
    return (
        <thead>
        <tr>
            {props.items.map((fieldName,index)=> (<th key={index}>{fieldName}</th>))}
        </tr>
        </thead>
    )
}


const StudentList = (props) => {
    console.log("list " + props.items)
    return (
            <div className={"container"}>
                <table className={"table table-hover"}>
                <TableHead items={['Name','Email Id', 'Date Of Birth', 'DB Folder']}/>
                <tbody>
                {props.items.map((student) => 
                <StudentItem student={student} key={student.id}/>
                )}
                </tbody>
                </table>
            </div>
    );
}

class StudentListContainer extends Component{
    
    cookies = new Cookies();
    constructor(props) {
        super(props);
        this.state = { list: [] }
    }
    
    componentDidMount() {
        this.props.updateHeading('All Students');
        // fetch(`http://127.0.0.1:8000/onlineapp/api/v1/colleges/${this.props.match.params.id}/students/`,
        fetch(`http://127.0.0.1:8000/onlineapp/api/v1/colleges/${this.props.match.params.id}/students/`, { 
            method: 'get', 
            headers: new Headers({
            'Authorization': 'JWT '+this.cookies.get('userJwtToken').token, 
            }), 
            })
            .then(function(response) {
                return response.json();
            })
            .then((myJson) => {
                console.log(myJson);
                this.setState(prev => ( {list : myJson}));
            })
            .catch(e => {console.log("Error occured in fetching students..")});
    }

    render(){
        console.log("TodoItemContainer");
        console.log(this.state.list)
        
        return <StudentList items={this.state.list}/>;
    }
}

export default StudentListContainer