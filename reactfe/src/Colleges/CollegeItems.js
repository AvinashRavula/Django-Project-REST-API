import React, { Component } from 'react'
import { Link } from "react-router-dom"

const CollegeItem = (props) => {
    return (
        <tr>
            <td><Link to={`/college/${props.college.id}`}>{props.college.name}</Link></td>
            <td>{props.college.acronym}</td>
            <td>{props.college.location}</td>
            <td>{props.college.contact}</td>
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


const CollegeList = (props) => {
    console.log("list " + props.items)
    return (
            <div className={"container"}>
                <table className={"table table-hover"}>
                <TableHead items={['Name','Acronym', 'Location', 'Contact']}/>
                <tbody>
                {props.items.map((college) => 
                <CollegeItem college={college} key={college.id}/>
                )}
                </tbody>
                </table>
            </div>
    );
}

export default CollegeList