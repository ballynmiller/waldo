import Body from './components/body';
import Header from './components/header';

var $ = require('jquery')
var React = require('react');
var reactDom = require('react-dom');


var Waldo = React.createClass({
    getInitialState: function(){
        return {
            data: JSON.parse(sessionStorage.getItem("feeds")) || [],
        };
    },
    buttonSearch: function(text){
        $.ajax({
            url: "http://localhost:5000/feeds/" + text,
            type: "GET",
            success: function(data){
                this.setState({
                    data: data['feeds']
                });
                sessionStorage.setItem("feeds", JSON.stringify(data['feeds']));
                sessionStorage.setItem("text", text);
            }.bind(this)
        });
    },
    render: function(){
        return (
            <div>
                <Header
                    handleClick={this.buttonSearch}
                />
                <Body
                    data={this.state.data}
                />
            </div>
        );
    }
});

reactDom.render(
        <Waldo />,
        $('#app').get(0)
);
