import React from 'react';
import ReactDOM from 'react-dom';

class oneDish extends React.component{
	constructor(props){
		super(props);
		this.state={ count: 0};
		this.handleAddOne = this.handleAddOne.bind(this);
		this.handleMinusOne = this.handleMinusOne.bind(this);
	}
	
	handleAddOne(){
		const newCount = this.state.count+1;
		this.setState({count : newCount});
	}
	
	handleMinusOne(){
		const newCount = this.state.count-1;
		newCount = newCount > 0? newCount :0;
		this.setState({count :newCount});
	}
	
	render(){
		return {
			<div>
				<div>{this.props.name}</div>
				<button onClick = {this.handleMinusOne}>-</button>
				<div>{this.state.count}</div>
				<button onClick = {this.handleAddOne}>+</button>
			</div>
		};
	}
}