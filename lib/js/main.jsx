import Body from './components/body';
import Header from './components/header';

var React = require('react');
var reactDom = require ('react-dom');
var $ = require('jquery');


class Waldo extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            data: JSON.parse(sessionStorage.getItem("feeds")) || [],
            loading: false,
            queried: false,
        }

        this._bind('searchHandler');
    }

    _bind(...methods){
        methods.forEach(method => this[method] = this[method].bind(this));
    }

    searchHandler(text) {
        this.setState({loading: true});

        $.ajax({
            url: "http://localhost:5000/feeds/" + text,
            type: "GET",
            success: function(data){
                this.setState({
                    data: data['feeds'],
                });
                sessionStorage.setItem("feeds", JSON.stringify(data['feeds']));
                sessionStorage.setItem("text", text);
            }.bind(this)
        }).always(function(){
            this.setState({
                queried: true,
                loading: false
            });
        }.bind(this));
    }

    render(){
        return (
            <div>
                <Header
                    searchHandler={this.searchHandler}
                    loading={this.state.loading}
                />
                <Body
                    results={this.state.data}
                    queried={this.state.queried}
                />
            </div>
        );
    }
}

reactDom.render(
        <Waldo />,
        $('#app').get(0)
);
